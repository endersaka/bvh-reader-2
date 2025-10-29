import sys
from antlr4 import *
from BVHLexer import BVHLexer
from BVHParser import BVHParser
from BVHListener import BVHListener


def main(argv):
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
        print(tree.toStringTree(recog=parser))

        print("\nParsing completed successfully!")

    except Exception as e:
        print(f"Error while parsing: {str(e)}")


if __name__ == '__main__':
    main(sys.argv)
