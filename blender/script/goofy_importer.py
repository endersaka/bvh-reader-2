""" Goofy BVH Importer for Blender is not a module, but a script to be run
    inside Blender's scripting environment.
    Though, since Pylance/Pyright complains about missing module docstrings,
    we add this here.
    """

# First import system wide modules
import enum
import sys
import os
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

if WORKINGENVIRONMENT == WorkingEnvironment.BLENDER:
    # FIXME: this funcion does nothing for the moment, MakeHuman community Asset Pack BVH files
    # seem to already be in Z-up coordinate system.
    def bvh_to_blender_coords(bvh_offset: Vector) -> Vector:
        """
        Converts a BVH (X, Y, Z) offset vector to Blender's coordinate system
        (typically Z-up, Y-forward).
        A common transformation for BVH to Blender is (X, Y, Z) -> (X, Z, -Y).
        """
        x, y, z = bvh_offset
        # return Vector((x, z, -y))
        return Vector((x, y, z))  # No conversion for now

    # NOTE: Possible function for applying the first frame's joint|root transform.

    def calc_frame_transform(edit_bone_head, node_frame_coordinates):
        """ Calculate the transformation matrix for a joint/node/segment

        Args:
            node_world_position (mathutils.Vector): Vector rappresenting a position relative to World Space
            node_frame_coordinates (list | tuple): list of float values that can have 3 or 6 elements 

        Returns:
            mathutils.Matrix: A 4x4 matrix carrying the result transformation
        """

        # TODO: we are not validating parameters.

        # Previously, we were assuming that each node channels were 6, though
        # sometimes only the root segment owns 6 channels, while the other joint
        # segments have only 3 channels.
        channel_rotations = node_frame_coordinates[3:6]
        if len(node_frame_coordinates) < 6:
            channel_rotations = node_frame_coordinates

        rot_mat4 = Euler([radians(channel)
                         for channel in channel_rotations]).to_matrix().to_4x4()
        rot_mat4[0][3] += edit_bone_head.x
        rot_mat4[1][3] += edit_bone_head.y
        rot_mat4[2][3] += edit_bone_head.z
        return rot_mat4

    def create_bones(
        edit_bones: bpy.types.ArmatureEditBones,
        joint_data: dict,
        parent_edit_bone: bpy.types.EditBone
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

        joint_name = joint_data.get("name")
        if joint_name == "End Site":
            # End Sites do not become bones themselves
            return

        # Offset is relative to the parent joint's head world position.
        offset_vec = Vector(joint_data['offset'])
        blender_offset = bvh_to_blender_coords(offset_vec)

        # Calculate the current joint's world head position
        current_head_world_pos = parent_edit_bone.head + blender_offset

        # Create the new bone
        # Use the joint name, or a default if missing.
        bone_name = joint_name if joint_name else "Joint"

        # TODO: I think this can be handled more elegantly?
        # Handle duplicate names by incrementing if necessary
        # (Blender does this automatically if a name already exists,
        # But we need to ensure we use the actual resulting name for the parent link).
        if bone_name in edit_bones:
            # Use a counter to ensure unique names (e.g., bone_name.001)
            i = 1
            while f"{bone_name}.{i:03d}" in edit_bones:
                i += 1
            bone_name = f"{bone_name}.{i:03d}"

        # Finally create the bone
        new_bone = edit_bones.new(bone_name)
        new_bone.head = current_head_world_pos
        new_bone.parent = edit_bones.get(parent_edit_bone.name)

        # Determine the current bone's tip position
        children = joint_data.get("children", [])

        end_site_child = next(
            (c for c in children if c.get("name") == "End Site"), None)

        if end_site_child:
            # Rule: "End Site" named nodes serve to place the bone tip of their parent node.
            end_site_offset = bvh_to_blender_coords(
                Vector(end_site_child["offset"]))
            new_bone.tail = current_head_world_pos + end_site_offset

        elif children:
            # Rule: The tips of parent bones should just use the offset of (let's say) the first child bone.
            first_child_joint = next(
                (c for c in children if c.get("name") != "End Site"), None)

            if first_child_joint:
                # The tip is the world position (head) of the first child joint.
                first_child_offset = Vector(first_child_joint["offset"])
                blender_first_child_offset = bvh_to_blender_coords(
                    first_child_offset)
                new_bone.tail = current_head_world_pos + blender_first_child_offset
            else:
                # Fallback for joints whose only children are 'End Site' nodes (handled by the if end_site_child check)
                # or for a malformed hierarchy. Since the End Site check is first, this fallback is less likely.
                new_bone.tail = current_head_world_pos + \
                    Vector((0.0, 0.0, 0.1))  # Small length along Z-axis (up)

        else:
            # TODO: I would eventually extrude the tail along the direction of the parent bone?
            # Leaf bone without an End Site
            new_bone.tail = current_head_world_pos + \
                Vector((0.0, 0.0, 0.1))  # Small length along Z-axis (up)

        # Recursively call for all non-End Site children
        for child_data in children:
            if child_data.get("name") != "End Site":
                create_bones(
                    edit_bones,
                    child_data,
                    new_bone
                )

    def pose_armature():
        pass

    def build_armature_from_bvh_dict(bvh_structure: dict):
        """
        Main function to initialize the Blender Armature and start the recursive build.
        """

        global node_frame_data_index, TRANSFORMS

        # Prepare the armature object
        armature_data = bpy.data.armatures.new("BVH_Armature_Data")
        armature_object = bpy.data.objects.new("BVH_Armature", armature_data)
        bpy.context.collection.objects.link(armature_object)
        print(
            f"Created Armature Object {armature_object.name}: {armature_object.name in bpy.context.collection.objects}")

        # Deselect all and select the new armature
        bpy.ops.object.select_all(action='DESELECT')
        armature_object.select_set(True)
        bpy.context.view_layer.objects.active = armature_object
        print(
            f"Selected Armature Object: {bpy.context.view_layer.objects.active.name}")

        # Switch to Edit Mode to create bones
        bpy.ops.object.mode_set(mode='EDIT')
        print("Switched to Edit Mode")

        # Is a collection of EditBone objects which allow to edit armature bones.
        # specific type of collection: https://docs.blender.org/api/4.2/bpy.types.ArmatureEditBones.html
        # https://docs.blender.org/api/4.2/bpy.types.bpy_prop_collection.html
        # https://docs.blender.org/api/4.2/bpy.types.EditBone.html
        edit_bones = armature_data.edit_bones
        print(f"Edit Bones Collection: {edit_bones}")

        # Get the Root Node (the 'hierarchy' object)
        root_data = bvh_structure["hierarchy"]
        print(
            f"Data collected for Root Joint: {root_data.get('name', 'Unnamed Root!!!!!!!')}")


        # We assume that the BVH file follows a Y Up, -Z Forward convention,
        # and convert accordingly.
        # NOTE: disabled. MH BVHs are already in Z up.
        #
        # Enforce BPY naming conventions.
        # `bpy.types.EditBone.head` is a `mathutils.Vector`, relative to
        # Armature Space.
        # In Blender, the Head of a Bone represents its rotation pivot.
        #print("BVH offset data of root joint: " + root_data["offset"])
        offset_vec = bvh_to_blender_coords(Vector(root_data["offset"]))
        print(f"Offset `mathutils.Vector` (in Blender coords system): {offset_vec}")

        # NOTE: we use a counter to access per frame vector components,
        # we have to do so, until we change the frame data structure.
        #
        # The set off coordinate components associated to root joint at
        # frame 0.
        frame_coords = bvh_structure['motion']['motion_data'][0][0]
        print(f"Root joint frame coordinate components: {frame_coords}")

        # Compute the transformation of the bone in the first frame.
        pose_bone_mat4 = calc_frame_transform(offset_vec, frame_coords)
        print(f"Pose root bone transformation matrix at frame 0: {pose_bone_mat4}")
        
        # Store the calculated matrix into `TRANSFORMS`.
        TRANSFORMS.append({'root': pose_bone_mat4})
        print(f"Store the pose bone transformation: {TRANSFORMS}")

        # Create the Root Bone
        root_bone = edit_bones.new(root_data.get('name', 'root'))
        root_bone.head = offset_vec
        root_bone.parent = None
        print(f"Created Root Bone: {root_bone.name} at {root_bone.head}")

        # TODO: actually here we would like to compute a midpoint of the root
        # head and its children heads.
        root_children = root_data.get("children", [])
        if root_children:
            first_child = next(
                (c for c in root_children if c.get("name") != "End Site"), None)

            # Set root bone tail vector to the value of its first child offset.
            if first_child:
                # NOTE: again, the possibly useless conversion.
                root_bone.tail = offset_vec + \
                    bvh_to_blender_coords(Vector(first_child["offset"]))
            else:
                # Fallback for a single-joint hierarchy
                root_bone.tail = offset_vec + Vector((0.0, 0.0, 0.1))
        else:
            root_bone.tail = offset_vec + Vector((0.0, 0.0, 0.1))

        # Recursively create children bones
        for child_data in root_children:
            create_bones(
                edit_bones,
                child_data,
                root_bone
            )

        # Switch back to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
        print(f"Successfully created Armature: {armature_object.name}")

    def init_blender_scene():
        """ Initialize the Blender scene for Armature building. """
        # Clear any selection and ensure we are in a mode that allows object creation
        if bpy.context.object and bpy.context.object.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        # Clear existing objects in the scene before running
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)


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

            # Import the BVH structure into Blender as an Armature
            build_armature_from_bvh_dict(bvh_dict)
            print(f'TRANSFORMS: {TRANSFORMS}')

        except Exception as e:
            print(f"Error while building Blender Armature: {str(e)}")
