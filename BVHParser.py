# Generated from BVH.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,112,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,43,8,
        3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,3,1,3,1,4,1,4,3,4,55,8,4,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,4,8,75,8,8,11,8,12,8,76,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,5,10,90,8,10,10,10,12,10,93,9,10,1,11,4,11,96,8,11,
        11,11,12,11,97,1,11,3,11,101,8,11,1,12,1,12,1,13,3,13,106,8,13,1,
        13,1,13,3,13,110,8,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,0,2,1,0,12,17,1,0,23,24,106,0,28,1,0,0,0,2,32,1,0,0,0,4,35,
        1,0,0,0,6,39,1,0,0,0,8,54,1,0,0,0,10,56,1,0,0,0,12,60,1,0,0,0,14,
        66,1,0,0,0,16,71,1,0,0,0,18,78,1,0,0,0,20,80,1,0,0,0,22,95,1,0,0,
        0,24,102,1,0,0,0,26,105,1,0,0,0,28,29,3,2,1,0,29,30,3,20,10,0,30,
        31,5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,34,3,4,2,0,34,3,1,0,0,0,
        35,36,5,2,0,0,36,37,3,24,12,0,37,38,3,6,3,0,38,5,1,0,0,0,39,40,5,
        18,0,0,40,42,3,14,7,0,41,43,3,16,8,0,42,41,1,0,0,0,42,43,1,0,0,0,
        43,47,1,0,0,0,44,46,3,8,4,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,
        0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,19,0,0,51,
        7,1,0,0,0,52,55,3,10,5,0,53,55,3,12,6,0,54,52,1,0,0,0,54,53,1,0,
        0,0,55,9,1,0,0,0,56,57,5,3,0,0,57,58,3,24,12,0,58,59,3,6,3,0,59,
        11,1,0,0,0,60,61,5,4,0,0,61,62,5,5,0,0,62,63,5,18,0,0,63,64,3,14,
        7,0,64,65,5,19,0,0,65,13,1,0,0,0,66,67,5,6,0,0,67,68,3,26,13,0,68,
        69,3,26,13,0,69,70,3,26,13,0,70,15,1,0,0,0,71,72,5,7,0,0,72,74,5,
        23,0,0,73,75,3,18,9,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,
        76,77,1,0,0,0,77,17,1,0,0,0,78,79,7,0,0,0,79,19,1,0,0,0,80,81,5,
        8,0,0,81,82,5,9,0,0,82,83,5,20,0,0,83,84,5,23,0,0,84,85,5,10,0,0,
        85,86,5,11,0,0,86,87,5,20,0,0,87,91,3,26,13,0,88,90,3,22,11,0,89,
        88,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,21,1,0,0,
        0,93,91,1,0,0,0,94,96,3,26,13,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,
        1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,101,5,26,0,0,100,99,1,0,
        0,0,100,101,1,0,0,0,101,23,1,0,0,0,102,103,5,21,0,0,103,25,1,0,0,
        0,104,106,5,22,0,0,105,104,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,
        0,107,109,7,1,0,0,108,110,5,25,0,0,109,108,1,0,0,0,109,110,1,0,0,
        0,110,27,1,0,0,0,9,42,47,54,76,91,97,100,105,109
    ]

class BVHParser ( Parser ):

    grammarFileName = "BVH.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'HIERARCHY'", "'ROOT'", "'JOINT'", "'End'", 
                     "'Site'", "'OFFSET'", "'CHANNELS'", "'MOTION'", "'Frames'", 
                     "'Frame'", "'Time'", "'Xposition'", "'Yposition'", 
                     "'Zposition'", "'Xrotation'", "'Yrotation'", "'Zrotation'", 
                     "'{'", "'}'", "':'" ]

    symbolicNames = [ "<INVALID>", "HIERARCHY", "ROOT", "JOINT", "END", 
                      "SITE", "OFFSET", "CHANNELS", "MOTION", "FRAMES", 
                      "FRAME", "TIME", "Xposition", "Yposition", "Zposition", 
                      "Xrotation", "Yrotation", "Zrotation", "LBRACE", "RBRACE", 
                      "COLON", "IDENT", "SIGN", "INT", "FLOAT", "EXP", "NL", 
                      "WS", "COMMENT" ]

    RULE_bvh = 0
    RULE_hierarchy = 1
    RULE_root = 2
    RULE_node = 3
    RULE_childBlock = 4
    RULE_joint = 5
    RULE_endSite = 6
    RULE_offset = 7
    RULE_channels = 8
    RULE_channelType = 9
    RULE_motion = 10
    RULE_frameLine = 11
    RULE_identifier = 12
    RULE_number = 13

    ruleNames =  [ "bvh", "hierarchy", "root", "node", "childBlock", "joint", 
                   "endSite", "offset", "channels", "channelType", "motion", 
                   "frameLine", "identifier", "number" ]

    EOF = Token.EOF
    HIERARCHY=1
    ROOT=2
    JOINT=3
    END=4
    SITE=5
    OFFSET=6
    CHANNELS=7
    MOTION=8
    FRAMES=9
    FRAME=10
    TIME=11
    Xposition=12
    Yposition=13
    Zposition=14
    Xrotation=15
    Yrotation=16
    Zrotation=17
    LBRACE=18
    RBRACE=19
    COLON=20
    IDENT=21
    SIGN=22
    INT=23
    FLOAT=24
    EXP=25
    NL=26
    WS=27
    COMMENT=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BvhContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hierarchy(self):
            return self.getTypedRuleContext(BVHParser.HierarchyContext,0)


        def motion(self):
            return self.getTypedRuleContext(BVHParser.MotionContext,0)


        def EOF(self):
            return self.getToken(BVHParser.EOF, 0)

        def getRuleIndex(self):
            return BVHParser.RULE_bvh

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBvh" ):
                listener.enterBvh(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBvh" ):
                listener.exitBvh(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBvh" ):
                return visitor.visitBvh(self)
            else:
                return visitor.visitChildren(self)




    def bvh(self):

        localctx = BVHParser.BvhContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_bvh)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.hierarchy()
            self.state = 29
            self.motion()
            self.state = 30
            self.match(BVHParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HierarchyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HIERARCHY(self):
            return self.getToken(BVHParser.HIERARCHY, 0)

        def root(self):
            return self.getTypedRuleContext(BVHParser.RootContext,0)


        def getRuleIndex(self):
            return BVHParser.RULE_hierarchy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHierarchy" ):
                listener.enterHierarchy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHierarchy" ):
                listener.exitHierarchy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHierarchy" ):
                return visitor.visitHierarchy(self)
            else:
                return visitor.visitChildren(self)




    def hierarchy(self):

        localctx = BVHParser.HierarchyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hierarchy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(BVHParser.HIERARCHY)
            self.state = 33
            self.root()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOT(self):
            return self.getToken(BVHParser.ROOT, 0)

        def identifier(self):
            return self.getTypedRuleContext(BVHParser.IdentifierContext,0)


        def node(self):
            return self.getTypedRuleContext(BVHParser.NodeContext,0)


        def getRuleIndex(self):
            return BVHParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = BVHParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(BVHParser.ROOT)
            self.state = 36
            self.identifier()
            self.state = 37
            self.node()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(BVHParser.LBRACE, 0)

        def offset(self):
            return self.getTypedRuleContext(BVHParser.OffsetContext,0)


        def RBRACE(self):
            return self.getToken(BVHParser.RBRACE, 0)

        def channels(self):
            return self.getTypedRuleContext(BVHParser.ChannelsContext,0)


        def childBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BVHParser.ChildBlockContext)
            else:
                return self.getTypedRuleContext(BVHParser.ChildBlockContext,i)


        def getRuleIndex(self):
            return BVHParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNode" ):
                return visitor.visitNode(self)
            else:
                return visitor.visitChildren(self)




    def node(self):

        localctx = BVHParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(BVHParser.LBRACE)
            self.state = 40
            self.offset()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 41
                self.channels()


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 44
                self.childBlock()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(BVHParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChildBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def joint(self):
            return self.getTypedRuleContext(BVHParser.JointContext,0)


        def endSite(self):
            return self.getTypedRuleContext(BVHParser.EndSiteContext,0)


        def getRuleIndex(self):
            return BVHParser.RULE_childBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChildBlock" ):
                listener.enterChildBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChildBlock" ):
                listener.exitChildBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChildBlock" ):
                return visitor.visitChildBlock(self)
            else:
                return visitor.visitChildren(self)




    def childBlock(self):

        localctx = BVHParser.ChildBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_childBlock)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.joint()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.endSite()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOINT(self):
            return self.getToken(BVHParser.JOINT, 0)

        def identifier(self):
            return self.getTypedRuleContext(BVHParser.IdentifierContext,0)


        def node(self):
            return self.getTypedRuleContext(BVHParser.NodeContext,0)


        def getRuleIndex(self):
            return BVHParser.RULE_joint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoint" ):
                listener.enterJoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoint" ):
                listener.exitJoint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoint" ):
                return visitor.visitJoint(self)
            else:
                return visitor.visitChildren(self)




    def joint(self):

        localctx = BVHParser.JointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_joint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BVHParser.JOINT)
            self.state = 57
            self.identifier()
            self.state = 58
            self.node()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndSiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(BVHParser.END, 0)

        def SITE(self):
            return self.getToken(BVHParser.SITE, 0)

        def LBRACE(self):
            return self.getToken(BVHParser.LBRACE, 0)

        def offset(self):
            return self.getTypedRuleContext(BVHParser.OffsetContext,0)


        def RBRACE(self):
            return self.getToken(BVHParser.RBRACE, 0)

        def getRuleIndex(self):
            return BVHParser.RULE_endSite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndSite" ):
                listener.enterEndSite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndSite" ):
                listener.exitEndSite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndSite" ):
                return visitor.visitEndSite(self)
            else:
                return visitor.visitChildren(self)




    def endSite(self):

        localctx = BVHParser.EndSiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_endSite)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(BVHParser.END)
            self.state = 61
            self.match(BVHParser.SITE)
            self.state = 62
            self.match(BVHParser.LBRACE)
            self.state = 63
            self.offset()
            self.state = 64
            self.match(BVHParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OFFSET(self):
            return self.getToken(BVHParser.OFFSET, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BVHParser.NumberContext)
            else:
                return self.getTypedRuleContext(BVHParser.NumberContext,i)


        def getRuleIndex(self):
            return BVHParser.RULE_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOffset" ):
                listener.enterOffset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOffset" ):
                listener.exitOffset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOffset" ):
                return visitor.visitOffset(self)
            else:
                return visitor.visitChildren(self)




    def offset(self):

        localctx = BVHParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_offset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(BVHParser.OFFSET)
            self.state = 67
            self.number()
            self.state = 68
            self.number()
            self.state = 69
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHANNELS(self):
            return self.getToken(BVHParser.CHANNELS, 0)

        def INT(self):
            return self.getToken(BVHParser.INT, 0)

        def channelType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BVHParser.ChannelTypeContext)
            else:
                return self.getTypedRuleContext(BVHParser.ChannelTypeContext,i)


        def getRuleIndex(self):
            return BVHParser.RULE_channels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChannels" ):
                listener.enterChannels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChannels" ):
                listener.exitChannels(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChannels" ):
                return visitor.visitChannels(self)
            else:
                return visitor.visitChildren(self)




    def channels(self):

        localctx = BVHParser.ChannelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_channels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(BVHParser.CHANNELS)
            self.state = 72
            self.match(BVHParser.INT)
            self.state = 74 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self.channelType()
                self.state = 76 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Xposition(self):
            return self.getToken(BVHParser.Xposition, 0)

        def Yposition(self):
            return self.getToken(BVHParser.Yposition, 0)

        def Zposition(self):
            return self.getToken(BVHParser.Zposition, 0)

        def Xrotation(self):
            return self.getToken(BVHParser.Xrotation, 0)

        def Yrotation(self):
            return self.getToken(BVHParser.Yrotation, 0)

        def Zrotation(self):
            return self.getToken(BVHParser.Zrotation, 0)

        def getRuleIndex(self):
            return BVHParser.RULE_channelType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChannelType" ):
                listener.enterChannelType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChannelType" ):
                listener.exitChannelType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChannelType" ):
                return visitor.visitChannelType(self)
            else:
                return visitor.visitChildren(self)




    def channelType(self):

        localctx = BVHParser.ChannelTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_channelType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MotionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOTION(self):
            return self.getToken(BVHParser.MOTION, 0)

        def FRAMES(self):
            return self.getToken(BVHParser.FRAMES, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BVHParser.COLON)
            else:
                return self.getToken(BVHParser.COLON, i)

        def INT(self):
            return self.getToken(BVHParser.INT, 0)

        def FRAME(self):
            return self.getToken(BVHParser.FRAME, 0)

        def TIME(self):
            return self.getToken(BVHParser.TIME, 0)

        def number(self):
            return self.getTypedRuleContext(BVHParser.NumberContext,0)


        def frameLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BVHParser.FrameLineContext)
            else:
                return self.getTypedRuleContext(BVHParser.FrameLineContext,i)


        def getRuleIndex(self):
            return BVHParser.RULE_motion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMotion" ):
                listener.enterMotion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMotion" ):
                listener.exitMotion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMotion" ):
                return visitor.visitMotion(self)
            else:
                return visitor.visitChildren(self)




    def motion(self):

        localctx = BVHParser.MotionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_motion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(BVHParser.MOTION)
            self.state = 81
            self.match(BVHParser.FRAMES)
            self.state = 82
            self.match(BVHParser.COLON)
            self.state = 83
            self.match(BVHParser.INT)
            self.state = 84
            self.match(BVHParser.FRAME)
            self.state = 85
            self.match(BVHParser.TIME)
            self.state = 86
            self.match(BVHParser.COLON)
            self.state = 87
            self.number()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 88
                self.frameLine()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FrameLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BVHParser.NumberContext)
            else:
                return self.getTypedRuleContext(BVHParser.NumberContext,i)


        def NL(self):
            return self.getToken(BVHParser.NL, 0)

        def getRuleIndex(self):
            return BVHParser.RULE_frameLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrameLine" ):
                listener.enterFrameLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrameLine" ):
                listener.exitFrameLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrameLine" ):
                return visitor.visitFrameLine(self)
            else:
                return visitor.visitChildren(self)




    def frameLine(self):

        localctx = BVHParser.FrameLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_frameLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 94
                    self.number()

                else:
                    raise NoViableAltException(self)
                self.state = 97 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 99
                self.match(BVHParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BVHParser.IDENT, 0)

        def getRuleIndex(self):
            return BVHParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = BVHParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BVHParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BVHParser.FLOAT, 0)

        def INT(self):
            return self.getToken(BVHParser.INT, 0)

        def SIGN(self):
            return self.getToken(BVHParser.SIGN, 0)

        def EXP(self):
            return self.getToken(BVHParser.EXP, 0)

        def getRuleIndex(self):
            return BVHParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = BVHParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 104
                self.match(BVHParser.SIGN)


            self.state = 107
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 108
                self.match(BVHParser.EXP)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





