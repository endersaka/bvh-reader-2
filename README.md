# BVH Reader 2

BVH Reader 2 is a BVH (BioVision Hierarcy) file reader written in Python 3. It is generated with Antlr4, starting from a grammar: [`.\BVH.g4`](https://github.com/endersaka/bvh-reader-2/blob/main/BVH.g4).

> **NOTE**: the number '2' in the name of this project is not a version number. It is a nostalgic addition, taken from my former project [MD5 Reader 2](https://sourceforge.net/projects/md5reader/), in which I implemented (manually) my first Lexer/Parser code.


## Dependecies

The base scripts are built on top of Antlr4, therefore, you have to install the runtime package.

```shell
python -m pip install antlr4-python3-runtime
```

or just

```shell
pip install antlr4-python3-runtime
```

Some code in the `./blender/script` directory, needs to be run inside of [Blender](https://www.blender.org), by opening the script inside the [Blender *Text Editor*](https://docs.blender.org/manual/en/4.2/editors/text_editor.html). To run a script inside the Text Editor press `ALT-P` or press the play button in the UI.
The Blender version I am currently using for this project is [Blender 4.2.1 LTS](https://www.blender.org/download/releases/4-2/).

To install the Antlr4 runtime in the Blender Python environment you should invoke the Python executable insalled inside your Blender installation directory.
On Windows 11, Blender installer places the application directory wherever you choose, though, the default directory shoud be `C:\Program Files\`, to which is appended `.\Blender Foundation\Blender 4.2\` and, finally, Python stuff is inside `.\4.2\python\`. If you don't have permissions to install Python packages into the installation Blender directory, `pip` automaticaly falls back to `C:\Users\<username>\AppData\Roaming\Python\Python311\Scripts`, which is actually desiderable.

```powershell
& "C:\Program Files\Blender Foundation\Blender 4.2\4.2\python\bin\python.exe" -m pip show antlr4-python3-runtime
```

## Usage

To extract the data from a BVH file you can use the `BVHListener` or the `BVHVisitor`. For more details on how to use Antlr4 listeners and visitors visit the [Antlr4 official website](https://www.antlr.org/).

`./harness.py` test script, should work this way:

```shell
python harness.py test.bvh
```

It outputs the Antrl4 tree.


## Disclaimer

**This is a early implementation, I didn't test it myself, yet.** Updates will come soon.


## History

This project borns as an ancillary project of [MPFB](https://extensions.blender.org/add-ons/mpfb/) Extension for [Blender](https://blender.org). Official MPFB developer team are not involved (yet) in my effor/test, neither they have approved it. BVH Reader 2 is my own endeavour, to date.