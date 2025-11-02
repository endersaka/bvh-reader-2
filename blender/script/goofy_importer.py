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
import logging
import json
from functools import reduce
from typing import Sequence
from math import radians
from antlr4 import FileStream, CommonTokenStream

logger = logging.getLogger(__name__)


class WorkingEnvironment(enum.Enum):
    """ Enum to represent the working environment: Blender or Standalone script. """
    BLENDER = 1
    STANDALONE = 2


WORKINGENVIRONMENT = WorkingEnvironment.STANDALONE

# Determine the working environment
try:
    import bpy
    from mathutils import Vector, Euler, Matrix

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

if WORKINGENVIRONMENT == WorkingEnvironment.BLENDER:
    REST_POSE = []

    def compute_midpoint(points: Sequence[Vector] | None) -> Vector:
        """ Compute the mid point of a sequence of `mathutils.Vector` objects

        Args:
            vectors (Sequence[Vector]): The sequence of vectors

        Returns:
            Vector: the mid point Vector
        """
        if points is None:
            return Vector((.0, .0, .1))
        
        mp = reduce(lambda v1, v2: v1 + v2, points) / len(points)
        print(f'midpoint: {mp}')

        return mp

    def bvh_to_blender_axis(components):
        """
        Converts a BVH (X, Y, Z) offset vector to Blender's coordinate system
        (typically Z-up, Y-forward).
        A common transformation for BVH to Blender is (X, Y, Z) -> (X, Z, -Y).
        """
        x, y, z = components
        return (x, z, -y)

    def euler_from_components(transform_components):
        """ Calculate Euler transformation given the rotations on the 3 axes

        Args:
            transform_components (Sequence): Sequence of float values 

        Returns:
            mathutils.Euler: rotation transformation
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
        return Euler([radians(channel) for channel in rotation_components])

    def create_bones(
        armature_data,
        segment_data: dict,
        parent_edit_bone: bpy.types.EditBone,
        bvh: dict
    ):
        """Recursively creates a bone for the current joint, setting
        its head, parent, and then determining its tip based on
        children/End Site rules.

        Args:
            edit_bones (bpy.types.ArmatureEditBones): armature data block used to edit bones rest pose
            joint_data (dict): joint data dictionary from BVH
            parent_edit_bone (bpy.types.EditBone): parent EditBone
        """

        edit_bones = armature_data.edit_bones

        # Use the joint name, or a default if missing.
        bone_name = segment_data.get('name', 'bone')

        # Handle duplicate names by incrementing if necessary
        if bone_name in edit_bones:
            # Use a counter to ensure unique names (e.g., bone_name.001)
            i = 1
            while f'{bone_name}.{i:03d}' in edit_bones:
                i += 1
            bone_name = f'{bone_name}.{i:03d}'

        # Create `bpy.types.EditBone`.
        edit_bone = edit_bones.new(bone_name)
        print(f'Edit bone "{edit_bone.name}" created.')

        # Calculate and apply the bone head vector.
        #
        # Offset, as extracted by BVH file, is a triplet of float values
        # recording the current joint position, relative to its parent
        # position.
        # `bpy.types.EditBone.head`, instead, is a `mathutils.Vector`,
        # relative to Armature Space. A bone head, in Blender, is the
        # bone's rotation pivot.
        edit_bone.parent = parent_edit_bone
        if edit_bone.parent is None:
            edit_bone.head = Vector(segment_data['offset'])
        else:
            edit_bone.head = edit_bone.parent.head + \
                Vector(segment_data['offset'])

        # Determine bone's tail position
        children = segment_data.get('children')
        if children is not None and len(children) > 0:
            # If the mapped segment has just one child, we place the
            # bone's tail at the child segment offset. 
            if len(children) == 1:
                edit_bone.tail = edit_bone.head + Vector(children[0]["offset"])

            # It the mapped segment, instead, has more than one child,
            # we compute the children midpoint and place the bone's
            # tail at that location.
            elif len(children) > 1:
                edit_bone.tail = edit_bone.head + \
                    compute_midpoint([Vector(child.get('offset'))
                                     for child in children])
        # In case (theoretically non normative in BVH format, but:
        # who knows?) that the segment has no child, we just offset
        # the bone's tail a bit along Z.
        else:
            edit_bone.tail = edit_bone.head + Vector((0.0, 0.0, 0.1))

        bones = armature_data.bones

        print(f'Bones count: {len(bones)}')
        # For use later in sandwich computation, rest pose matrix and inverse matrix.
        bone_rest_pose = bones[edit_bone.name].matrix_local.to_3x3()
        bone_rest_pose_inv = Matrix(bone_rest_pose).invert_safe()

        # Append the results to `REST_POSE`.
        REST_POSE.append({
            'name': edit_bone.name,
            'rest_pose': bone_rest_pose.resize_4x4(),
            'rest_pose_inv': bone_rest_pose_inv.resize_4x4()
        })

        # Recursively traverse the hierarchy and create descendant bone
        for child_data in children:
            # `End Site` blocks serve only as terminators of the hierarchy.
            # Don't go further!
            if child_data.get('name') != 'End Site':
                create_bones(
                    armature_data,
                    child_data,
                    edit_bone,
                    bvh
                )

    def create_armature() -> bpy.types.Armature:
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

        return armature_data

    def init_blender_scene():
        """ Initialize the Blender scene for Armature building. """
        # Clear any selection and ensure we are in a mode that allows object creation
        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        # Clear existing objects in the scene before running
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

    def pose_bones(motion):
        """" bla bla """

        # Switch to Edit Mode to create bones
        bpy.ops.object.mode_set(mode='POSE')
        print("Switched to Pose Mode")

        frame_data = motion.get('motion_data')[0]
        print(f'frame_motion_data: {frame_data}')

        for segment_motion_data in frame_data:
            print(f'segment_motion_data: {segment_motion_data}')
            segment_name = segment_motion_data.get('name')
            pose_bone = bpy.context.object.pose.bones[segment_name]

            components = (
                radians(segment_motion_data.get('Xrotation')),
                radians(segment_motion_data.get('Yrotation')),
                radians(segment_motion_data.get('Zrotation'))
            )

            bone_rest_pose_data = [b for b in REST_POSE if b.get('name') == segment_name]
            bone_rest_pose_mat4 = bone_rest_pose_data.get('rest_pose')
            bone_rest_pose_inv_mat4 = bone_rest_pose_data.get('rest_pose_inv')
            euler = Euler(components, 'ZXY')
            # sandwich
            bone_rotation_mat4 = (
                bone_rest_pose_inv_mat4 @
                euler.to_matrix().to_4x4() @
                bone_rest_pose_mat4
            )

            # Get bone rotation mode and apply transform accordingly.
            rotation_mode = pose_bone.rotation_mode
            if rotation_mode == 'QUATERNION':
                pose_bone.rotation_quaternion = bone_rotation_mat4.to_quaternion()
            elif rotation_mode == 'EULER':
                pose_bone.rotation_euler = bone_rotation_mat4.to_euler(order='ZXY')

# TODO: check at https://docs.blender.org/api/4.2/mathutils.html#mathutils.Euler,
# there is a simpler example using `format()`.
def serialize_euler(obj):
    """ Bla, bla, bla, ... """
    if isinstance(obj, Euler):
        return {
            'x_rot': obj.x,
            'y_rot': obj.y,
            'z_rot': obj.z
        }
    raise TypeError(f'Cannot serialize object of {type(obj)}')

if __name__ == "__main__":
    # Apparently, the `FileHandler` automatically instanced by `basicConfig()`
    # doesn't create missing directories in the `filename` parameter (another
    # undocumented thing), therefore, we have to handle it.
    log_dir = os.path.join(project_root, 'log')
    # Create the directory, if it doesn't exist.
    os.makedirs(log_dir, exist_ok=True)

    # I guess (I haven't found any enlightening documentation, to date) that
    # the default base directory is set relative to the execution environment.
    # In fact, Python outputs the following error:
    # PermissionError: [Errno 13] Permission denied: 'D:\\Program Files\\Blender Foundation\\Blender 4.2\\goofy_importer.log'
    # 'D:\\Program Files\\Blender Foundation\\Blender 4.2\\' is the location
    # of my Blender executable.
    # Therefore, I have to set a different location, which, for now, is set
    # to the project root.
    logging.basicConfig(filename=os.path.join(log_dir, 'goofy_importer.log'), level=logging.NOTSET)
    logger.info('Logger Started')

    # Where to store the parsed BVH structure
    bvh = None  # pylint: disable=invalid-name

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
        bvh = v.visit(tree)

        print(f"Total visited nodes: {v.nodes_count}")

        print("\nParsing completed successfully!")

    except Exception as e:
        print(f"Error while parsing: {str(e)}")

    # Build the Blender Armature if in Blender environment
    if WORKINGENVIRONMENT == WorkingEnvironment.BLENDER:
        try:
            init_blender_scene()

            armature_data = create_armature()
            # `bpy.types.ArmatureEditBones`: collection of `EditBone` objects.
            

            create_bones(
                armature_data,
                bvh.get('hierarchy'),
                None,
                bvh
            )

            pose_bones(bvh.get('motion'))

            # Switch back to Object Mode
            bpy.ops.object.mode_set(mode='OBJECT')

        except Exception as e:
            print("Traceback Info:")
            traceback.print_exc()

    logger.info('Logger Stopped')
