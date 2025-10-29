# Generated from BVH.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BVHParser import BVHParser
else:
    from BVHParser import BVHParser

# This class defines a complete generic visitor for a parse tree produced by BVHParser.

class BVHVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BVHParser#bvh.
    def visitBvh(self, ctx:BVHParser.BvhContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#hierarchy.
    def visitHierarchy(self, ctx:BVHParser.HierarchyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#root.
    def visitRoot(self, ctx:BVHParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#node.
    def visitNode(self, ctx:BVHParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#childBlock.
    def visitChildBlock(self, ctx:BVHParser.ChildBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#joint.
    def visitJoint(self, ctx:BVHParser.JointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#endSite.
    def visitEndSite(self, ctx:BVHParser.EndSiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#offset.
    def visitOffset(self, ctx:BVHParser.OffsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#channels.
    def visitChannels(self, ctx:BVHParser.ChannelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#channelType.
    def visitChannelType(self, ctx:BVHParser.ChannelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#motion.
    def visitMotion(self, ctx:BVHParser.MotionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#frameLine.
    def visitFrameLine(self, ctx:BVHParser.FrameLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#identifier.
    def visitIdentifier(self, ctx:BVHParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BVHParser#number.
    def visitNumber(self, ctx:BVHParser.NumberContext):
        return self.visitChildren(ctx)



del BVHParser