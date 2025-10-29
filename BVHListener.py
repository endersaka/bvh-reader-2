# Generated from BVH.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BVHParser import BVHParser
else:
    from BVHParser import BVHParser

# This class defines a complete listener for a parse tree produced by BVHParser.
class BVHListener(ParseTreeListener):

    # Enter a parse tree produced by BVHParser#bvh.
    def enterBvh(self, ctx:BVHParser.BvhContext):
        pass

    # Exit a parse tree produced by BVHParser#bvh.
    def exitBvh(self, ctx:BVHParser.BvhContext):
        pass


    # Enter a parse tree produced by BVHParser#hierarchy.
    def enterHierarchy(self, ctx:BVHParser.HierarchyContext):
        pass

    # Exit a parse tree produced by BVHParser#hierarchy.
    def exitHierarchy(self, ctx:BVHParser.HierarchyContext):
        pass


    # Enter a parse tree produced by BVHParser#root.
    def enterRoot(self, ctx:BVHParser.RootContext):
        pass

    # Exit a parse tree produced by BVHParser#root.
    def exitRoot(self, ctx:BVHParser.RootContext):
        pass


    # Enter a parse tree produced by BVHParser#node.
    def enterNode(self, ctx:BVHParser.NodeContext):
        pass

    # Exit a parse tree produced by BVHParser#node.
    def exitNode(self, ctx:BVHParser.NodeContext):
        pass


    # Enter a parse tree produced by BVHParser#childBlock.
    def enterChildBlock(self, ctx:BVHParser.ChildBlockContext):
        pass

    # Exit a parse tree produced by BVHParser#childBlock.
    def exitChildBlock(self, ctx:BVHParser.ChildBlockContext):
        pass


    # Enter a parse tree produced by BVHParser#joint.
    def enterJoint(self, ctx:BVHParser.JointContext):
        pass

    # Exit a parse tree produced by BVHParser#joint.
    def exitJoint(self, ctx:BVHParser.JointContext):
        pass


    # Enter a parse tree produced by BVHParser#endSite.
    def enterEndSite(self, ctx:BVHParser.EndSiteContext):
        pass

    # Exit a parse tree produced by BVHParser#endSite.
    def exitEndSite(self, ctx:BVHParser.EndSiteContext):
        pass


    # Enter a parse tree produced by BVHParser#offset.
    def enterOffset(self, ctx:BVHParser.OffsetContext):
        pass

    # Exit a parse tree produced by BVHParser#offset.
    def exitOffset(self, ctx:BVHParser.OffsetContext):
        pass


    # Enter a parse tree produced by BVHParser#channels.
    def enterChannels(self, ctx:BVHParser.ChannelsContext):
        pass

    # Exit a parse tree produced by BVHParser#channels.
    def exitChannels(self, ctx:BVHParser.ChannelsContext):
        pass


    # Enter a parse tree produced by BVHParser#channelType.
    def enterChannelType(self, ctx:BVHParser.ChannelTypeContext):
        pass

    # Exit a parse tree produced by BVHParser#channelType.
    def exitChannelType(self, ctx:BVHParser.ChannelTypeContext):
        pass


    # Enter a parse tree produced by BVHParser#motion.
    def enterMotion(self, ctx:BVHParser.MotionContext):
        pass

    # Exit a parse tree produced by BVHParser#motion.
    def exitMotion(self, ctx:BVHParser.MotionContext):
        pass


    # Enter a parse tree produced by BVHParser#frameLine.
    def enterFrameLine(self, ctx:BVHParser.FrameLineContext):
        pass

    # Exit a parse tree produced by BVHParser#frameLine.
    def exitFrameLine(self, ctx:BVHParser.FrameLineContext):
        pass


    # Enter a parse tree produced by BVHParser#identifier.
    def enterIdentifier(self, ctx:BVHParser.IdentifierContext):
        pass

    # Exit a parse tree produced by BVHParser#identifier.
    def exitIdentifier(self, ctx:BVHParser.IdentifierContext):
        pass


    # Enter a parse tree produced by BVHParser#number.
    def enterNumber(self, ctx:BVHParser.NumberContext):
        pass

    # Exit a parse tree produced by BVHParser#number.
    def exitNumber(self, ctx:BVHParser.NumberContext):
        pass



del BVHParser