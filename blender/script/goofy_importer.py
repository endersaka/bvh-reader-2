""" Goofy BVH Importer for Blender is not a module, but a script to be run
    inside Blender's scripting environment.
    Though, since Pylance/Pyright complains about missing module docstrings,
    we add this here.
    """

# First import system wide modules
import enum
import sys
import os
import traceback
from typing import Sequence
from math import radians
from antlr4 import FileStream, CommonTokenStream


class WorkingEnvironment(enum.Enum):
    """ Enum to represent the working environment: Blender or Standalone script. """
    BLENDER = 1
    STANDALONE = 2


WORKINGENVIRONMENT = WorkingEnvironment.STANDALONE

# Determine the working environment
try:
    import bpy
    from mathutils import Vector, Euler

    print("Running inside Blender")
    WORKINGENVIRONMENT = WorkingEnvironment.BLENDER
except ImportError:
    print("Running outside Blender")

CONTEXTSYSPATHS = []
script_dir = ''

if WORKINGENVIRONMENT == WorkingEnvironment.BLENDER:
    # Get the current script being executed
    text = bpy.context.space_data.text

    if text.filepath:
        # If the script is saved, retrieve its directory
        script_dir = os.path.dirname(bpy.path.abspath(text.filepath))
    else:
        print("The script is not saved. Please save it to retrieve the directory.")
        exit(1)
elif WORKINGENVIRONMENT == WorkingEnvironment.STANDALONE:
    # Get the directory where this script is located ('./blender/script' relative to project root),
    # and the project root directory (2 levels up from `script_dir`).
    # NOTE: we are assuming that the structure is 'ProjectRoot/blender/script/goofy_importer.py'.
    # FIXME: this is going to fail in Blender, if we just open the script from the Text Editor,
    # since __file__ is not defined there. We need to find another way to get the project root
    # in that case, perhaps by using bpy.path or similar Blender-specific APIs.
    script_dir = os.path.dirname(os.path.realpath(__file__))

print("Script Directory:", script_dir)

project_root = os.path.join(script_dir, '..', '..')
print("Project root:", project_root)

CONTEXTSYSPATHS.append(script_dir)
CONTEXTSYSPATHS.append(project_root)

# Add all the gathered paths to sys.path if not already present.
for path in CONTEXTSYSPATHS:
    if path not in sys.path:
        sys.path.append(path)

# Now you can import your Antlr files as if you were in the root
# Assuming your Antlr files are MyGrammarLexer.py, MyGrammarParser.py, etc.
try:
    from BVHParser import BVHParser
    from BVHLexer import BVHLexer
    from BPYBVHVisitor import BPYBVHVisitor

    print("Successfully imported Antlr files!")
except ImportError as e:
    print(f"Error importing Antlr files: {e}")


node_frame_data_index = 0
TRANSFORMS = []


def append_transform(segment_name, transform):
    """ Convenience function to append new transforms to `TRANSFORMS` list, as
        a more structured data.

    Args:
        segment_name (String): the name of the `JOINT` or `ROOT` segment
        transform (mathutils.Euler | mathutils.Quaternion | mathutils.Matrix): transformation
    """
    TRANSFORMS.append({
        'segment_name': segment_name,
        'transform': transform
    })


if WORKINGENVIRONMENT == WorkingEnvironment.BLENDER:
    def compute_midpoint(points: Sequence[Vector] | None) -> Vector:
        """ Compute the mid point of a sequence of `mathutils.Vector` objects

        Args:
            vectors (Sequence[Vector]): The sequence of vectors

        Returns:
            Vector: the mid point Vector
        """
        if points is None:
            return Vector((.0, .0, .1))

        return sum(points) / len(points)

    def bvh_to_blender_axis(components):
        """
        Converts a BVH (X, Y, Z) offset vector to Blender's coordinate system
        (typically Z-up, Y-forward).
        A common transformation for BVH to Blender is (X, Y, Z) -> (X, Z, -Y).
        """
        x, y, z = components
        return (x, z, -y)

    # NOTE: Possible function for applying the first frame's joint|root transform.

    def euler_from_components(transform_components):
        """ Calculate the transformation matrix for a joint/node/segment

        Args:
            node_world_position (mathutils.Vector): Vector rappresenting a position relative to World Space
            node_frame_coordinates (list | tuple): list of float values that can have 3 or 6 elements 

        Returns:
            mathutils.Matrix: A 4x4 matrix carrying the result transformation
        """

        # TODO: we are not validating parameters.

        # Commonly, `ROOT` segment has 6 channels, while `JOINT` segments only 3.
        # We need to account for this possibility.
        if len(transform_components) < 6:
            rotation_components = transform_components
        else:
            rotation_components = transform_components[3:6]

        # This block is `PoseBone.rotation_mode` agnostic, so, all we can do is
        # calculating the euler rotation.
        return Euler([radians(channel) for channel in bvh_to_blender_axis(rotation_components)])

    def create_bones(
        edit_bones: bpy.types.ArmatureEditBones,
        joint_data: dict,
        parent_edit_bone: bpy.types.EditBone,
        bvh_structure: dict
    ):
        """Recursively creates a bone for the current joint, setting
        its head, parent, and then determining its tip based on
        children/End Site rules.

        Args:
            edit_bones (bpy.types.ArmatureEditBones): armature data block used to edit bones rest pose
            joint_data (dict): joint data dictionary from BVH
            parent_edit_bone (bpy.types.EditBone): parent EditBone
        """

        global node_frame_data_index, TRANSFORMS

        node_frame_data_index += 1

        #######################################################################
        # HERE BEGINS THE PART THAT IS NEARLY IDENTICAL IN `build_armature...`#
        #######################################################################

        # Use the joint name, or a default if missing.
        bone_name = joint_data.get('name', 'bone')

        # Handle duplicate names by incrementing if necessary
        if bone_name in edit_bones:
            # Use a counter to ensure unique names (e.g., bone_name.001)
            i = 1
            while f'{bone_name}.{i:03d}' in edit_bones:
                i += 1
            bone_name = f'{bone_name}.{i:03d}'

        # Create the `bpy.types.EditBone`.
        edit_bone = edit_bones.new(bone_name)

        # Offset components, as extracted by BVH file, represent a position
        # relative to the parent joint position.
        # Compute joint's head vector (which represent a armature space
        # relative position)

        # `bpy.types.EditBone.head` is a `mathutils.Vector`, relative to
        # Armature Space. In Blender, the Head of a Bone represents its
        # rotation pivot.
        edit_bone.parent = parent_edit_bone
        if edit_bone.parent is None:
            edit_bone.head = Vector(joint_data['offset'])
        else:
            edit_bone.head = edit_bone.parent.head + Vector(joint_data['offset'])

        # Determine bone's tail position
        children = joint_data.get('children')
        if children is not None and len(children) > 0:
            if len(children) == 1:
                edit_bone.tail = edit_bone.head + Vector(children[0]["offset"])

            elif len(children) > 1:
                edit_bone.tail = edit_bone.head + \
                    compute_midpoint([Vector(child.get('offset'))
                                     for child in children])

        else:
            # Add a small length along Z-axis (up)
            edit_bone.tail = edit_bone.head + Vector((0.0, 0.0, 0.1))

        # The set off coordinate components associated to the joint at
        # frame 0.
        # NOTE: we use a counter to access per frame vector components,
        # we have to do so, until we change the frame data structure.
        frame_coords = bvh_structure['motion']['motion_data'][0][node_frame_data_index]

        # Compute the transformation of the bone in the first frame.
        pose_bone_euler = euler_from_components(frame_coords)

        # Store the calculated matrix into `TRANSFORMS`.
        append_transform(bone_name, pose_bone_euler)

        # Recursively traverse the hierarchy and create descendant bone
        for child_data in children:
            # `End Site` blocks serve only as terminators of the hierarchy.
            # Don't go further!
            if child_data.get('name') != 'End Site':
                create_bones(
                    edit_bones,
                    child_data,
                    edit_bone,
                    bvh_structure
                )

    def build_armature_from_bvh_dict(bvh_structure: dict):
        """
        Main function to initialize the Blender Armature and start the recursive build.
        """

        global node_frame_data_index, TRANSFORMS

        # `bpy.types.ArmatureEditBones`: collection of `EditBone` objects.
        edit_bones = create_armature()

        # Root segment data
        root_data = bvh_structure["hierarchy"]

        #######################################################################
        #   HERE BEGINS THE PART THAT IS NEARLY IDENTICAL IN `create_bones`   #
        #######################################################################
        #
        # We assume that the BVH file follows a Y Up, -Z Forward convention,
        # and convert accordingly.

        # The set off coordinate components associated to root joint at
        # frame 0.
        # NOTE: we use a counter to access per frame vector components,
        # we have to do so, until we change the frame data structure.
        frame_coords = bvh_structure['motion']['motion_data'][0][node_frame_data_index]

        # Compute the transformation of the bone in the first frame.
        pose_bone_euler = euler_from_components(frame_coords)

        # Store the calculated matrix into `TRANSFORMS`.
        append_transform('root', pose_bone_euler)

        # Create the `bpy.types.EditBone`.
        root_bone = edit_bones.new(root_data.get('name', 'root'))

        # `bpy.types.EditBone.head` is a `mathutils.Vector`, relative to
        # Armature Space. In Blender, the Head of a Bone represents its
        # rotation pivot.
        root_bone.head = Vector(root_data["offset"])
        root_bone.parent = None
        print(f"Bone created: {root_bone.name} at {root_bone.head}")

        # Determine bone's tail position
        children = root_data.get('children')
        if children is not None and len(children) > 0:
            if len(children) == 1:
                root_bone.tail = root_bone.head + Vector(children[0]["offset"])
            
            elif len(children) > 1:
                root_bone.tail = root_bone.head + \
                    compute_midpoint([child.head for child in children])

        else:
            # Small length along Z-axis (up)
            root_bone.tail = root_bone.head + Vector((0.0, 0.0, 0.1))

        # Recursively traverse the hierarchy and create descendant bones
        for child_data in children:
            # `End Site` blocks serve only as terminators of the hierarchy.
            # Don't go further!
            if child_data.get('name') != 'End Site':
                create_bones(
                    edit_bones,
                    child_data,
                    root_bone,
                    bvh_structure
                )

        pose_armature()

        # Switch back to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')

    def create_armature():
        """ Create the armature, prepare the environment, and return a
            `bpy.types.ArmatureEditBones` collection ready for bones editing.
        """
        armature_data = bpy.data.armatures.new("BVH_Armature_Data")
        armature_object = bpy.data.objects.new("BVH_Armature", armature_data)
        bpy.context.collection.objects.link(armature_object)

        # Deselect all and select the newly created armature
        bpy.ops.object.select_all(action='DESELECT')
        armature_object.select_set(True)
        bpy.context.view_layer.objects.active = armature_object

        # Switch to Edit Mode to create bones
        bpy.ops.object.mode_set(mode='EDIT')
        print("Switched to Edit Mode")

        return armature_data.edit_bones

    def init_blender_scene():
        """ Initialize the Blender scene for Armature building. """
        # Clear any selection and ensure we are in a mode that allows object creation
        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        # Clear existing objects in the scene before running
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

    def pose_armature():
        """" bla bla """
        global TRANSFORMS

        # Switch to Edit Mode to create bones
        bpy.ops.object.mode_set(mode='POSE')
        print("Switched to Pose Mode")

        for transform in TRANSFORMS:
            pose_bone = bpy.context.object.pose.bones[transform['segment_name']]

            rotation_mode = pose_bone.rotation_mode
            # print(f'Rotation mode: {rotation_mode}')

            if rotation_mode == 'QUATERNION':
                pose_bone.rotation_quaternion = transform['transform'].to_quaternion(
                )
            elif rotation_mode == 'EULER':
                pose_bone.rotation_euler = transform['transform']


if __name__ == "__main__":
    # Where to store the parsed BVH structure
    bvh_dict = None  # pylint: disable=invalid-name

    # Get BVH file path
    bvh_filepath = os.path.join(project_root, 'test.bvh')

    # Parse the BVH file
    try:
        # Create an input stream from filepath
        input_stream = FileStream(bvh_filepath)

        # Create the lexer and the token stream
        lexer = BVHLexer(input_stream)
        stream = CommonTokenStream(lexer)

        # Create the parser consuming the token stream
        parser = BVHParser(stream)

        # Parse the BVH file, beginning from the `bvh` rule, defined in the grammar `./BVH.g4`
        tree = parser.bvh()

        # Log the parse tree (for debugging)
        # print(tree.toStringTree(recog=parser))

        v = BPYBVHVisitor()
        bvh_dict = v.visit(tree)

        print(f"Total visited nodes: {v.nodes_count}")

        print("\nParsing completed successfully!")

    except Exception as e:
        print(f"Error while parsing: {str(e)}")

    # Build the Blender Armature if in Blender environment
    if WORKINGENVIRONMENT == WorkingEnvironment.BLENDER:
        try:
            init_blender_scene()

            # `bpy.types.ArmatureEditBones`: collection of `EditBone` objects.
            edit_bones = create_armature()

            create_bones(
                edit_bones,
                bvh_dict.get('hierarchy'),
                None,
                bvh_dict
            )

            # Import the BVH structure into Blender as an Armature
            # build_armature_from_bvh_dict(bvh_dict)
            
            print(f'TRANSFORMS: {TRANSFORMS}')

        except Exception as e:
            print("Traceback Info:")
            traceback.print_exc()
