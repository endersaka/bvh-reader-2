# BVH Reader 2

BVH Reader 2 is a BVH (BioVision Hierarcy) file reader written in Python 3. It is generated with Antlr4, starting from a grammar: [`.\BVH.g4`](https://github.com/endersaka/bvh-reader-2/blob/main/BVH.g4).

> **NOTE**: the number '2' in the name of this project is not a version number. It is a nostalgic addition, taken from my former project [MD5 Reader 2](https://sourceforge.net/projects/md5reader/), in which I implemented (manually) my first Lexer/Parser code.


## Usage

To extract the data from a BVH file you can use the `BVHListener` or the `BVHVisitor`. For more details on how to use Antlr4 listeners and visitors visit the [Antlr4 official website](https://www.antlr.org/).


## Disclaimer

**This is a early implementation, I didn't test it myself, yet.** Updates will come soon.


## History

This project borns as an ancillary project of [MPFB](https://extensions.blender.org/add-ons/mpfb/) Extension for [Blender](https://blender.org). Official MPFB developer team are not involved (yet) in my effor/test, neither they have approved it. BVH Reader 2 is my own endeavour, to date.