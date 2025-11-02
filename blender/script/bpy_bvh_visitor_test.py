import json
import sys
import os
import traceback
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


def main(argv):
    """ Main function to parse BVH file and use BPYBVHVisitor. """

    # Check if file name is provided as argument
    if len(argv) < 2:
        print("Usage: python harness.py <input_file>")
        return

    # Get input file name from command line argument
    input_file = argv[1]

    try:
        # Create input stream from file
        input_stream = FileStream(input_file)

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
        data = v.visit(tree)
        
        # Write the data to a JSON file
        with open("tree.json", mode="w", encoding="utf-8") as tree_json_file:
            json.dump(data, tree_json_file, indent=4)
        
        # data contains nested dicts/lists for hierarchy and motion
        # print(data)

        print(f"Total nodes visited: {v.nodes_count}")

        print("\nParsing completed successfully!")

    except Exception as e:
        print("Traceback Info:")
        traceback.print_exc()


if __name__ == '__main__':
    main(sys.argv)
