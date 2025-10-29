"""Module providing a function printing python version."""

import sys
import os

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
    from BVHVisitor import BVHVisitor
    # ... other imports
    print("Successfully imported Antlr files!")
except ImportError as e:
    print(f"Error importing Antlr files: {e}")

class BPYBVHVisitor(BVHVisitor):
    """First Blender-specific visitor for BVH Visitor."""

    nodes_count = 0
    channels_count_per_node = []

    def visitBvh(self, ctx:BVHParser.BvhContext):
        hierarchy = self.visit(ctx.hierarchy())
        motion = self.visit(ctx.motion())
        return {"hierarchy": hierarchy, "motion": motion}

    def visitHierarchy(self, ctx:BVHParser.HierarchyContext):
        return self.visit(ctx.root())

    def visitRoot(self, ctx:BVHParser.RootContext):
        name = ctx.identifier().getText()
        node = self.visit(ctx.node())
        node["name"] = name
        return node

    def visitNode(self, ctx:BVHParser.NodeContext):
        # node: LBRACE offset channels? childBlock* RBRACE;
        offset = self.visit(ctx.offset())
        channels = self.visit(ctx.channels()) if ctx.channels() else []

        # Store channel count per node for later use
        self.channels_count_per_node.append(len(channels))

        children = [self.visit(c) for c in ctx.childBlock()] if ctx.childBlock() else []
        
        # Store total node count
        self.nodes_count += 1
        
        return {"offset": offset, "channels": channels, "children": children}

    def visitOffset(self, ctx:BVHParser.OffsetContext):
        return [float(ctx.number(i).getText()) for i in range(3)]

    def visitChannels(self, ctx:BVHParser.ChannelsContext):
        return [ctx.channelType(i).getText() for i in range(len(ctx.channelType()))]

    def visitJoint(self, ctx:BVHParser.JointContext):
        name = ctx.identifier().getText()
        node = self.visit(ctx.node())
        node["name"] = name
        return node

    def visitEndSite(self, ctx:BVHParser.EndSiteContext):
        return {"name": "End Site", "offset": self.visit(ctx.offset())}
    
    def visitMotion(self, ctx:BVHParser.MotionContext):
        num_frames = int(ctx.INT().getText())
        frame_time = float(ctx.number().getText())

        motion_data = []

        for frameline in ctx.frameLine():
            frames = []

            # This is a little complex because we need to map the flat list of numbers
            # to the hierarchical structure of nodes and their channels.
            #
            # We use `self.channels_count_per_node` to know how many channels each node has,
            # and we iterate through the numbers accordingly.
            #
            # `frameline.number()` gives us the list of numbers for the current frame.
            # We keep track of how many channels we've extracted for the current node,
            # and when we've extracted all channels for a node, we move to the next node by
            # incrementing `curr_node_index`.
            #
            # `extracted_channels_count` keeps track of how many channels we've extracted
            # for the current node so far.
            extracted_channels_count = 0

            # Initialize current node index, an keep track (in the loop) of the node we're
            # processing.
            curr_node_index = 0

            # List to hold the deltas (the float values associated to the node channels) for
            # the current node.
            curr_node_deltas = []
            for number in frameline.number():
                # Get the number of channels for the current node, previously stored in `self.visitNode()`.
                curr_node_channels_count = self.channels_count_per_node[curr_node_index]  

                # Store the coordinate
                curr_node_deltas.append(float(number.getText()))
                extracted_channels_count += 1

                # Move to the next node if we've extracted all its channels
                if extracted_channels_count >= curr_node_channels_count:
                    frames.append(curr_node_deltas)

                    # Reset for the next node
                    curr_node_deltas = []
                    extracted_channels_count = 0

                    # Increment the node index for the next iteration.
                    curr_node_index += 1

            motion_data.append(frames)
        
        return {"num_frames": num_frames, "frame_time": frame_time, "motion_data": motion_data}

    # implement other visit methods as needed
