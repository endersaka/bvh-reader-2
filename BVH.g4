grammar BVH;

/*
 Entry point: parse a full BVH file with HIERARCHY then MOTION. Usage (Python target): antlr4
 -Dlanguage=Python3 BVH.g4 python harness.py BVH bvh @Sit03Floor.txt --tree
 */

bvh: hierarchy motion EOF;

hierarchy: HIERARCHY root;

root: ROOT identifier node;

/*
 A node block: - starts with '{' - must contain exactly one OFFSET and one CHANNELS line (for
 joints), followed by zero or more child JOINT blocks or End Site blocks - ends with '}' Note: Some
 BVH variants put CHANNELS only on joints that have motion. This grammar accepts CHANNELS wherever
 present.
 */
node: LBRACE offset channels? childBlock* RBRACE;

childBlock: joint | endSite;

joint: JOINT identifier node;

endSite: END_SITE LBRACE offset RBRACE;

offset: OFFSET number number number;

/*
 CHANNELS format: CHANNELS <count> <channelType>... We don’t enforce the exact count here—runtime
 validation can.
 */
channels: CHANNELS INT channelType+;

channelType:
	Xposition
	| Yposition
	| Zposition
	| Xrotation
	| Yrotation
	| Zrotation;

/* MOTION section: Frames line, Frame Time line, then one or more frame lines (space-separated
 numbers).
 */
motion:
	MOTION FRAMES COLON INT FRAME_TIME COLON number frameLine*;

frameLine: number+ NL?;

/* Identifiers like "finger1-1.L" or "upperarm02.R" */
identifier: IDENT;

/* Numbers: integers, decimals, scientific notation */
number:
	SIGN? (FLOAT | INT) EXP?; // e.g., -0.123, 42, 1.2e-3, -5E+2

/* ---------------- Lexer rules ---------------- */

HIERARCHY: 'HIERARCHY';
ROOT: 'ROOT';
JOINT: 'JOINT';
END_SITE: 'End Site';
OFFSET: 'OFFSET';
CHANNELS: 'CHANNELS';
MOTION: 'MOTION';
FRAMES: 'Frames';
FRAME_TIME: 'Frame Time';

Xposition: 'Xposition';
Yposition: 'Yposition';
Zposition: 'Zposition';
Xrotation: 'Xrotation';
Yrotation: 'Yrotation';
Zrotation: 'Zrotation';

LBRACE: '{';
RBRACE: '}';
COLON: ':';

/* Identifier: letters, digits, underscore, dot, hyphen */
IDENT: [A-Za-z_] [A-Za-z0-9_.-]*;

/* Integers and floats */
SIGN: [+-];
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]* | '.' [0-9]+;

/* Scientific exponent (e/E[+/-]digits) */
EXP: [eE] [+-]? [0-9]+;

/* Newline (optional consumption in frameLine) */
NL: [\r\n]+ -> skip;

/* Whitespace (spaces, tabs) */
WS: [ \t\f]+ -> skip;

/* Comments (rare in BVH, but sometimes present with '#') */
COMMENT: '#' ~[\r\n]* -> skip;