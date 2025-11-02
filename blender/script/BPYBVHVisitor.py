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
    node_names = []
    hierarchy = None

    def _store_names(self, segment):
        self.node_names.append({
            'name': segment.get('name', 'unnamed_segment'),
            'channels': segment.get('channels', {})
        })

        children = segment.get('children')
        if children is not None:
            for child in children:
                if child.get('name') == 'End Site':
                    break
                self._store_names(child)


    def visitBvh(self, ctx:BVHParser.BvhContext):
        self.hierarchy = self.visit(ctx.hierarchy())
        self._store_names(self.hierarchy)

        motion = self.visit(ctx.motion())
        return {"hierarchy": self.hierarchy, "motion": motion}

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
        # Get motion data properties.
        num_frames = int(ctx.INT().getText())
        frame_time = float(ctx.number().getText())

        # `List` for storing elaborated motion data.
        motion_data = []

        # Compute every and each frame motion data.
        for frameline in ctx.frameLine():
            frame_motion_data = []

            # Index of the channel we are extracting for the current joint.
            channel_index = 0

            # Initialize current node index, an keep track (in the loop) of the node we're
            # processing.
            node_index = 0

            # `dict` where per node transforms are stored in the form:
            # {
            #     "name": 'spine01',
            #     "Xposition": 0.123,
            #     "Yposition": 0.123,
            #     "Zposition": 0.123,
            #     "Xrotation": 0.123,
            #     "Yrotation": 0.123,
            #     "Zrotation": 0.123
            # }
            node_motion_data = {}

            node_name = None
            node_channels = None

            # Add each channel `name: value` entry to the `dict` holding current node motion data.
            for number in frameline.number():
                if channel_index == 0:
                    # Node names have been stored in `self.node_names` by the method `self.visitJoint()`
                    # as a list, in reading order, so they can be used as a lookup table for frames.
                    node_name = self.node_names[node_index].get('name')
                    node_motion_data['name'] = node_name
                    
                    # Get current node channels, previously stored in `self.visitNode()`.
                    node_channels = self.node_names[node_index].get('channels')
                
                print(f'node_name: {node_name}')
                node_motion_data[node_channels[channel_index]] = float(number.getText())

                channel_index += 1

                # Move to the next node if we've extracted all its channels
                if channel_index >= len(node_channels):
                    # Append current node motion data to the current frame `List`.
                    frame_motion_data.append(node_motion_data)

                    # We have finished with the current node.
                    # We can reset the values for the next node.
                    node_motion_data = {}
                    channel_index = 0

                    # Increment the node index for the next iteration.
                    node_index += 1

            # Append the current frame motion data to `motion_data` `List`
            motion_data.append(frame_motion_data)
        
        # print(f'motion_data: {motion_data}')
        return {"num_frames": num_frames, "frame_time": frame_time, "motion_data": motion_data}

    # implement other visit methods as needed
