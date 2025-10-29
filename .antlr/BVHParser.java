// Generated from /home/endersaka/dev/antrl/test_bvh_grammar/BVH.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BVHParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		HIERARCHY=1, ROOT=2, JOINT=3, END=4, SITE=5, OFFSET=6, CHANNELS=7, MOTION=8, 
		FRAMES=9, FRAME=10, TIME=11, Xposition=12, Yposition=13, Zposition=14, 
		Xrotation=15, Yrotation=16, Zrotation=17, LBRACE=18, RBRACE=19, COLON=20, 
		IDENT=21, SIGN=22, INT=23, FLOAT=24, EXP=25, NL=26, WS=27, COMMENT=28;
	public static final int
		RULE_bvh = 0, RULE_hierarchy = 1, RULE_root = 2, RULE_node = 3, RULE_childBlock = 4, 
		RULE_joint = 5, RULE_endSite = 6, RULE_offset = 7, RULE_channels = 8, 
		RULE_channelType = 9, RULE_motion = 10, RULE_frameLine = 11, RULE_identifier = 12, 
		RULE_number = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"bvh", "hierarchy", "root", "node", "childBlock", "joint", "endSite", 
			"offset", "channels", "channelType", "motion", "frameLine", "identifier", 
			"number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'HIERARCHY'", "'ROOT'", "'JOINT'", "'End'", "'Site'", "'OFFSET'", 
			"'CHANNELS'", "'MOTION'", "'Frames'", "'Frame'", "'Time'", "'Xposition'", 
			"'Yposition'", "'Zposition'", "'Xrotation'", "'Yrotation'", "'Zrotation'", 
			"'{'", "'}'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "HIERARCHY", "ROOT", "JOINT", "END", "SITE", "OFFSET", "CHANNELS", 
			"MOTION", "FRAMES", "FRAME", "TIME", "Xposition", "Yposition", "Zposition", 
			"Xrotation", "Yrotation", "Zrotation", "LBRACE", "RBRACE", "COLON", "IDENT", 
			"SIGN", "INT", "FLOAT", "EXP", "NL", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BVH.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BVHParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BvhContext extends ParserRuleContext {
		public HierarchyContext hierarchy() {
			return getRuleContext(HierarchyContext.class,0);
		}
		public MotionContext motion() {
			return getRuleContext(MotionContext.class,0);
		}
		public TerminalNode EOF() { return getToken(BVHParser.EOF, 0); }
		public BvhContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bvh; }
	}

	public final BvhContext bvh() throws RecognitionException {
		BvhContext _localctx = new BvhContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_bvh);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			hierarchy();
			setState(29);
			motion();
			setState(30);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HierarchyContext extends ParserRuleContext {
		public TerminalNode HIERARCHY() { return getToken(BVHParser.HIERARCHY, 0); }
		public RootContext root() {
			return getRuleContext(RootContext.class,0);
		}
		public HierarchyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hierarchy; }
	}

	public final HierarchyContext hierarchy() throws RecognitionException {
		HierarchyContext _localctx = new HierarchyContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_hierarchy);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(HIERARCHY);
			setState(33);
			root();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public TerminalNode ROOT() { return getToken(BVHParser.ROOT, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public NodeContext node() {
			return getRuleContext(NodeContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(ROOT);
			setState(36);
			identifier();
			setState(37);
			node();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NodeContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(BVHParser.LBRACE, 0); }
		public OffsetContext offset() {
			return getRuleContext(OffsetContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(BVHParser.RBRACE, 0); }
		public ChannelsContext channels() {
			return getRuleContext(ChannelsContext.class,0);
		}
		public List<ChildBlockContext> childBlock() {
			return getRuleContexts(ChildBlockContext.class);
		}
		public ChildBlockContext childBlock(int i) {
			return getRuleContext(ChildBlockContext.class,i);
		}
		public NodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_node; }
	}

	public final NodeContext node() throws RecognitionException {
		NodeContext _localctx = new NodeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_node);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(LBRACE);
			setState(40);
			offset();
			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CHANNELS) {
				{
				setState(41);
				channels();
				}
			}

			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==JOINT || _la==END) {
				{
				{
				setState(44);
				childBlock();
				}
				}
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(50);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChildBlockContext extends ParserRuleContext {
		public JointContext joint() {
			return getRuleContext(JointContext.class,0);
		}
		public EndSiteContext endSite() {
			return getRuleContext(EndSiteContext.class,0);
		}
		public ChildBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_childBlock; }
	}

	public final ChildBlockContext childBlock() throws RecognitionException {
		ChildBlockContext _localctx = new ChildBlockContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_childBlock);
		try {
			setState(54);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case JOINT:
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				joint();
				}
				break;
			case END:
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				endSite();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JointContext extends ParserRuleContext {
		public TerminalNode JOINT() { return getToken(BVHParser.JOINT, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public NodeContext node() {
			return getRuleContext(NodeContext.class,0);
		}
		public JointContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joint; }
	}

	public final JointContext joint() throws RecognitionException {
		JointContext _localctx = new JointContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_joint);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(JOINT);
			setState(57);
			identifier();
			setState(58);
			node();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EndSiteContext extends ParserRuleContext {
		public TerminalNode END() { return getToken(BVHParser.END, 0); }
		public TerminalNode SITE() { return getToken(BVHParser.SITE, 0); }
		public TerminalNode LBRACE() { return getToken(BVHParser.LBRACE, 0); }
		public OffsetContext offset() {
			return getRuleContext(OffsetContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(BVHParser.RBRACE, 0); }
		public EndSiteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endSite; }
	}

	public final EndSiteContext endSite() throws RecognitionException {
		EndSiteContext _localctx = new EndSiteContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_endSite);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(END);
			setState(61);
			match(SITE);
			setState(62);
			match(LBRACE);
			setState(63);
			offset();
			setState(64);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OffsetContext extends ParserRuleContext {
		public TerminalNode OFFSET() { return getToken(BVHParser.OFFSET, 0); }
		public List<NumberContext> number() {
			return getRuleContexts(NumberContext.class);
		}
		public NumberContext number(int i) {
			return getRuleContext(NumberContext.class,i);
		}
		public OffsetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_offset; }
	}

	public final OffsetContext offset() throws RecognitionException {
		OffsetContext _localctx = new OffsetContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_offset);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(OFFSET);
			setState(67);
			number();
			setState(68);
			number();
			setState(69);
			number();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChannelsContext extends ParserRuleContext {
		public TerminalNode CHANNELS() { return getToken(BVHParser.CHANNELS, 0); }
		public TerminalNode INT() { return getToken(BVHParser.INT, 0); }
		public List<ChannelTypeContext> channelType() {
			return getRuleContexts(ChannelTypeContext.class);
		}
		public ChannelTypeContext channelType(int i) {
			return getRuleContext(ChannelTypeContext.class,i);
		}
		public ChannelsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_channels; }
	}

	public final ChannelsContext channels() throws RecognitionException {
		ChannelsContext _localctx = new ChannelsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_channels);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(CHANNELS);
			setState(72);
			match(INT);
			setState(74); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(73);
				channelType();
				}
				}
				setState(76); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 258048L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ChannelTypeContext extends ParserRuleContext {
		public TerminalNode Xposition() { return getToken(BVHParser.Xposition, 0); }
		public TerminalNode Yposition() { return getToken(BVHParser.Yposition, 0); }
		public TerminalNode Zposition() { return getToken(BVHParser.Zposition, 0); }
		public TerminalNode Xrotation() { return getToken(BVHParser.Xrotation, 0); }
		public TerminalNode Yrotation() { return getToken(BVHParser.Yrotation, 0); }
		public TerminalNode Zrotation() { return getToken(BVHParser.Zrotation, 0); }
		public ChannelTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_channelType; }
	}

	public final ChannelTypeContext channelType() throws RecognitionException {
		ChannelTypeContext _localctx = new ChannelTypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_channelType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 258048L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MotionContext extends ParserRuleContext {
		public TerminalNode MOTION() { return getToken(BVHParser.MOTION, 0); }
		public TerminalNode FRAMES() { return getToken(BVHParser.FRAMES, 0); }
		public List<TerminalNode> COLON() { return getTokens(BVHParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BVHParser.COLON, i);
		}
		public TerminalNode INT() { return getToken(BVHParser.INT, 0); }
		public TerminalNode FRAME() { return getToken(BVHParser.FRAME, 0); }
		public TerminalNode TIME() { return getToken(BVHParser.TIME, 0); }
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public List<FrameLineContext> frameLine() {
			return getRuleContexts(FrameLineContext.class);
		}
		public FrameLineContext frameLine(int i) {
			return getRuleContext(FrameLineContext.class,i);
		}
		public MotionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_motion; }
	}

	public final MotionContext motion() throws RecognitionException {
		MotionContext _localctx = new MotionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_motion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(MOTION);
			setState(81);
			match(FRAMES);
			setState(82);
			match(COLON);
			setState(83);
			match(INT);
			setState(84);
			match(FRAME);
			setState(85);
			match(TIME);
			setState(86);
			match(COLON);
			setState(87);
			number();
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) {
				{
				{
				setState(88);
				frameLine();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FrameLineContext extends ParserRuleContext {
		public List<NumberContext> number() {
			return getRuleContexts(NumberContext.class);
		}
		public NumberContext number(int i) {
			return getRuleContext(NumberContext.class,i);
		}
		public TerminalNode NL() { return getToken(BVHParser.NL, 0); }
		public FrameLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_frameLine; }
	}

	public final FrameLineContext frameLine() throws RecognitionException {
		FrameLineContext _localctx = new FrameLineContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_frameLine);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(95); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(94);
					number();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(97); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(100);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NL) {
				{
				setState(99);
				match(NL);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(BVHParser.IDENT, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(IDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberContext extends ParserRuleContext {
		public TerminalNode FLOAT() { return getToken(BVHParser.FLOAT, 0); }
		public TerminalNode INT() { return getToken(BVHParser.INT, 0); }
		public TerminalNode SIGN() { return getToken(BVHParser.SIGN, 0); }
		public TerminalNode EXP() { return getToken(BVHParser.EXP, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SIGN) {
				{
				setState(104);
				match(SIGN);
				}
			}

			setState(107);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EXP) {
				{
				setState(108);
				match(EXP);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001cp\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003+\b\u0003"+
		"\u0001\u0003\u0005\u0003.\b\u0003\n\u0003\f\u00031\t\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0003\u00047\b\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0004\bK\b\b\u000b\b"+
		"\f\bL\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0005\nZ\b\n\n\n\f\n]\t\n\u0001\u000b\u0004\u000b"+
		"`\b\u000b\u000b\u000b\f\u000ba\u0001\u000b\u0003\u000be\b\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0003\rj\b\r\u0001\r\u0001\r\u0003\rn\b\r\u0001\r\u0000"+
		"\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u0000\u0002\u0001\u0000\f\u0011\u0001\u0000\u0017\u0018j"+
		"\u0000\u001c\u0001\u0000\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u0004"+
		"#\u0001\u0000\u0000\u0000\u0006\'\u0001\u0000\u0000\u0000\b6\u0001\u0000"+
		"\u0000\u0000\n8\u0001\u0000\u0000\u0000\f<\u0001\u0000\u0000\u0000\u000e"+
		"B\u0001\u0000\u0000\u0000\u0010G\u0001\u0000\u0000\u0000\u0012N\u0001"+
		"\u0000\u0000\u0000\u0014P\u0001\u0000\u0000\u0000\u0016_\u0001\u0000\u0000"+
		"\u0000\u0018f\u0001\u0000\u0000\u0000\u001ai\u0001\u0000\u0000\u0000\u001c"+
		"\u001d\u0003\u0002\u0001\u0000\u001d\u001e\u0003\u0014\n\u0000\u001e\u001f"+
		"\u0005\u0000\u0000\u0001\u001f\u0001\u0001\u0000\u0000\u0000 !\u0005\u0001"+
		"\u0000\u0000!\"\u0003\u0004\u0002\u0000\"\u0003\u0001\u0000\u0000\u0000"+
		"#$\u0005\u0002\u0000\u0000$%\u0003\u0018\f\u0000%&\u0003\u0006\u0003\u0000"+
		"&\u0005\u0001\u0000\u0000\u0000\'(\u0005\u0012\u0000\u0000(*\u0003\u000e"+
		"\u0007\u0000)+\u0003\u0010\b\u0000*)\u0001\u0000\u0000\u0000*+\u0001\u0000"+
		"\u0000\u0000+/\u0001\u0000\u0000\u0000,.\u0003\b\u0004\u0000-,\u0001\u0000"+
		"\u0000\u0000.1\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000/0\u0001"+
		"\u0000\u0000\u000002\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u0000"+
		"23\u0005\u0013\u0000\u00003\u0007\u0001\u0000\u0000\u000047\u0003\n\u0005"+
		"\u000057\u0003\f\u0006\u000064\u0001\u0000\u0000\u000065\u0001\u0000\u0000"+
		"\u00007\t\u0001\u0000\u0000\u000089\u0005\u0003\u0000\u00009:\u0003\u0018"+
		"\f\u0000:;\u0003\u0006\u0003\u0000;\u000b\u0001\u0000\u0000\u0000<=\u0005"+
		"\u0004\u0000\u0000=>\u0005\u0005\u0000\u0000>?\u0005\u0012\u0000\u0000"+
		"?@\u0003\u000e\u0007\u0000@A\u0005\u0013\u0000\u0000A\r\u0001\u0000\u0000"+
		"\u0000BC\u0005\u0006\u0000\u0000CD\u0003\u001a\r\u0000DE\u0003\u001a\r"+
		"\u0000EF\u0003\u001a\r\u0000F\u000f\u0001\u0000\u0000\u0000GH\u0005\u0007"+
		"\u0000\u0000HJ\u0005\u0017\u0000\u0000IK\u0003\u0012\t\u0000JI\u0001\u0000"+
		"\u0000\u0000KL\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000LM\u0001"+
		"\u0000\u0000\u0000M\u0011\u0001\u0000\u0000\u0000NO\u0007\u0000\u0000"+
		"\u0000O\u0013\u0001\u0000\u0000\u0000PQ\u0005\b\u0000\u0000QR\u0005\t"+
		"\u0000\u0000RS\u0005\u0014\u0000\u0000ST\u0005\u0017\u0000\u0000TU\u0005"+
		"\n\u0000\u0000UV\u0005\u000b\u0000\u0000VW\u0005\u0014\u0000\u0000W[\u0003"+
		"\u001a\r\u0000XZ\u0003\u0016\u000b\u0000YX\u0001\u0000\u0000\u0000Z]\u0001"+
		"\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000"+
		"\\\u0015\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000^`\u0003\u001a"+
		"\r\u0000_^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000a_\u0001\u0000"+
		"\u0000\u0000ab\u0001\u0000\u0000\u0000bd\u0001\u0000\u0000\u0000ce\u0005"+
		"\u001a\u0000\u0000dc\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000"+
		"e\u0017\u0001\u0000\u0000\u0000fg\u0005\u0015\u0000\u0000g\u0019\u0001"+
		"\u0000\u0000\u0000hj\u0005\u0016\u0000\u0000ih\u0001\u0000\u0000\u0000"+
		"ij\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000km\u0007\u0001\u0000"+
		"\u0000ln\u0005\u0019\u0000\u0000ml\u0001\u0000\u0000\u0000mn\u0001\u0000"+
		"\u0000\u0000n\u001b\u0001\u0000\u0000\u0000\t*/6L[adim";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}