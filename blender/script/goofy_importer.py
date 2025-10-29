import bpy
from mathutils import Vector
import sys
import os
from antlr4 import FileStream, CommonTokenStream
from BPYBVHVisitor import BPYBVHVisitor

# 1. Get the directory of the current script (./blender/script)
script_dir = os.path.dirname(os.path.realpath(__file__))

# 2. Get the project root directory (one level up from script_dir)
# This assumes your structure is: ProjectRoot/blender/script/your_script.py
# If it's ProjectRoot/blender/script/your_script.py and Antlr files are in ProjectRoot
project_root = os.path.join(script_dir, '..', '..')

# 3. Add the project root to the system path
if project_root not in sys.path:
    sys.path.append(project_root)

# Now you can import your Antlr files as if you were in the root
# Assuming your Antlr files are MyGrammarLexer.py, MyGrammarParser.py, etc.
try:
    from BVHParser import BVHParser
    from BVHLexer import BVHLexer
    # ... other imports
    print("Successfully imported Antlr files!")
except ImportError as e:
    print(f"Error importing Antlr files: {e}")


def bvh_to_blender_coords(bvh_offset: Vector) -> Vector:
    """
    Converts a BVH (X, Y, Z) offset vector to Blender's coordinate system (typically Z-up, Y-forward).
    A common transformation for BVH to Blender is (X, Y, Z) -> (X, Z, -Y).
    """
    x, y, z = bvh_offset
    return Vector((x, z, -y))

def create_bone_recursive(
    edit_bones: bpy.types.EditBone,
    joint_data: dict,
    parent_bone_name: str,
    parent_world_pos: Vector
):
    """
    Recursively creates a bone for the current joint, setting its head, parent,
    and then determining its tip based on children/End Site rules.
    """
    joint_name = joint_data.get("name")
    if joint_name == "End Site":
        # End Sites do not become bones themselves
        return

    # 1. Calculate the current joint's world head position
    # Offset is relative to the parent joint's head world position.
    local_offset = Vector(joint_data["offset"])
    blender_offset = bvh_to_blender_coords(local_offset)
    current_head_world_pos = parent_world_pos + blender_offset

    # 2. Create the new bone
    # Use the joint name, or a default if missing
    bone_name = joint_name if joint_name else "Joint"
    
    # Handle duplicate names by incrementing if necessary (Blender does this automatically if a name already exists, 
    # but we need to ensure we use the actual resulting name for the parent link).
    if bone_name in edit_bones:
         # Use a counter to ensure unique names (e.g., bone_name.001)
         i = 1
         while f"{bone_name}.{i:03d}" in edit_bones:
             i += 1
         bone_name = f"{bone_name}.{i:03d}"
         
    new_bone = edit_bones.new(bone_name)
    new_bone.head = current_head_world_pos
    new_bone.parent = edit_bones.get(parent_bone_name)

    # 3. Determine the current bone's tip position
    children = joint_data.get("children", [])
    
    end_site_child = next((c for c in children if c.get("name") == "End Site"), None)
    
    if end_site_child:
        # Rule: "End Site" named nodes serve to place the bone tip of their parent node.
        end_site_offset = bvh_to_blender_coords(Vector(end_site_child["offset"]))
        new_bone.tail = current_head_world_pos + end_site_offset
        
    elif children:
        # Rule: The tips of parent bones should just use the offset of (let's say) the first child bone.
        first_child_joint = next((c for c in children if c.get("name") != "End Site"), None)
        
        if first_child_joint:
            # The tip is the world position (head) of the first child joint.
            first_child_offset = Vector(first_child_joint["offset"])
            blender_first_child_offset = bvh_to_blender_coords(first_child_offset)
            new_bone.tail = current_head_world_pos + blender_first_child_offset
        else:
            # Fallback for joints whose only children are 'End Site' nodes (handled by the if end_site_child check)
            # or for a malformed hierarchy. Since the End Site check is first, this fallback is less likely.
            new_bone.tail = current_head_world_pos + Vector((0.0, 0.0, 0.1)) # Small length along Z-axis (up)
            
    else:
        # Leaf bone without an End Site
        new_bone.tail = current_head_world_pos + Vector((0.0, 0.0, 0.1)) # Small length along Z-axis (up)

    # 4. Recursively call for all non-End Site children
    for child_data in children:
        if child_data.get("name") != "End Site":
            create_bone_recursive(
                edit_bones,
                child_data,
                parent_bone_name=bone_name,
                parent_world_pos=current_head_world_pos
            )

def build_armature_from_bvh_structure(bvh_structure: dict):
    """
    Main function to initialize the Blender Armature and start the recursive build.
    """
    # 1. Prepare the armature object
    armature_data = bpy.data.armatures.new("BVH_Armature_Data")
    armature_object = bpy.data.objects.new("BVH_Armature", armature_data)
    bpy.context.collection.objects.link(armature_object)
    
    # Deselect all and select the new armature
    bpy.ops.object.select_all(action='DESELECT')
    armature_object.select_set(True)
    bpy.context.view_layer.objects.active = armature_object

    # 2. Switch to Edit Mode to create bones
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = armature_data.edit_bones

    # 3. Handle the Root Node (the 'hierarchy' object)
    # The root joint typically has no parent, its offset is its world position.
    root_joint_data = bvh_structure["hierarchy"]
    root_name = "Hips" 
    
    # The root's position in world space
    root_offset = Vector(root_joint_data["offset"])
    root_world_pos = bvh_to_blender_coords(root_offset)

    # Create the Root Bone
    root_bone = edit_bones.new(root_name)
    root_bone.head = root_world_pos
    root_bone.parent = None

    # Determine Root Tip: use the offset of the first child joint
    root_children = root_joint_data.get("children", [])
    if root_children:
        first_child = next((c for c in root_children if c.get("name") != "End Site"), None)
        if first_child:
            # The tip is the head of the first child joint.
            first_child_offset = Vector(first_child["offset"])
            blender_first_child_offset = bvh_to_blender_coords(first_child_offset)
            root_bone.tail = root_world_pos + blender_first_child_offset
        else:
            # Fallback for a single-joint hierarchy
            root_bone.tail = root_world_pos + Vector((0.0, 0.0, 0.1))
    else:
        root_bone.tail = root_world_pos + Vector((0.0, 0.0, 0.1))


    # 4. Recursively create children bones
    for child_data in root_children:
        # The recursion starts with the children of the 'hierarchy' root
        create_bone_recursive(
            edit_bones,
            child_data,
            parent_bone_name=root_name,
            parent_world_pos=root_world_pos
        )

    # 5. Return to Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')
    print(f"Successfully created Armature: {armature_object.name}")

if __name__ == "__main__":
    BVHSTRUCTURE = None

    # Clear any selection and ensure we are in a mode that allows object creation
    if bpy.context.object and bpy.context.object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
        
    # Clear existing objects in the scene before running
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Get input file name from command line argument
    INPUT_FILE = '../../test.bvh'

    try:
        # Create input stream from file
        input_stream = FileStream(INPUT_FILE)

        # Create lexer
        lexer = BVHLexer(input_stream)
        stream = CommonTokenStream(lexer)

        # Create parser
        parser = BVHParser(stream)

        # Parse the input starting from the 'bvh' rule
        tree = parser.bvh()
        
        # Print parse tree (for debugging)
        # print(tree.toStringTree(recog=parser))

        v = BPYBVHVisitor()
        BVH_STRUCTURE = v.visit(tree)
        
        print(f"Total nodes visited: {v.nodes_count}")

        print("\nParsing completed successfully!")
        
        # Run the importer
        build_armature_from_bvh_structure(BVH_STRUCTURE)
    
    except Exception as e:
        print(f"Error while parsing: {str(e)}")
