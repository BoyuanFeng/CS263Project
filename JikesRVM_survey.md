# What is Jikes RVM
Jikes RVM is a virtual machine that runs Java programs. Unlike most other JVMs, it is written in Java, a style of
implementation termed meta-circular. Jikes RVM runs on many platforms. These platforms includes IA-32 Linux and PowerPC 64
Linux which are well supported and OS X, Solaris and PowerPC 32 which are less well-supported. It advances the state-of-the-
art of virtual machine technologies for dynamic compilation, adaptive optimization, garbage collection, thread scheduling, and 
synchronization. A distinguishing characteristic of Jikes RVM is that it is implemented in the Java™ programming language and 
is self-hosted i.e., its Java code runs on itself without requiring a second virtual machine. Most other virtual machines for 
the Java platform are written in native code (typically, C or C++). A Java implementation provides ease of portability, and a 
seamless integration of virtual machine and application resources such as objects, threads, and operating-system interfaces.

# How to Install Jikes RVM
## Get the Source
A developer can either work with the version control system or download one of the releases. If you are interested in doing 
development of Jikes RVM you should probably use Git instead of downloading a release.

### Download a Release
All the releases can be downloaded at [here](https://sourceforge.net/projects/jikesrvm/files/), you can use your web browser 
to download the latest version of Jikes RVM and uncompress it using the command below:
```
$ tar xvzf jikesrvm-<version>.tar.gz
```
or for the tar-bzip2 archive type:
```
$ tar xvjf jikesrvm-<version>.tar.bz2
```

### Use Git
If you're only interested in doing development of Jikes RVM (for our case we want ot measure the performance differences 
between different virtual machines) it's better to use git to install JIKes RVM.
If you are not familiar with Git, you can ﬁnd instructions on Git use at http://www.git-scm.com/doc. There is also a [Git 
book](https://www.git-scm.com/book/en/v2).
After installing Git the current version of source can be downloaded via:
```
$ git clone https://github.com/JikesRVM/JikesRVM.git
```
This will clone the Jikes RVM repository into the newly created directory jikesrvm.
If you need a speciﬁc version, it is recommended to clone the complete repository nonetheless. You can then switch to a 
speciﬁc release, e.g. 2.4.6, by doing the following:
```
$ cd jikesrvm 
$ git checkout 2.4.6
```

### Detailed Process
<img src="https://github.com/BoyuanFeng/CS263Project/blob/master/Installation_JikesRVM.png">

## Building Jikes RVM
Once you’ve met the requisite dependencies you can use the buildit script to build the system faster and easier. To avoid 
problems with the build, make sure that the path to the Jikes RVM source code doesn’t contain any whitespace.

### Target Requirements
Note that x86_64 is currently only supported using the legacy 32bit addressing mode and instructions. You need to install the 
32-bit versions of the required libraries to build and use the x86_64 conﬁgurations.

### Tool Requirements

Java Virtual Machine, Ant, C compilers, Bison, Perl, Awk.

### Building Process

#### Deﬁning Ant Properties
There are lots of ant properties you can configure for the build process of Jikes RVM, Figure below shows the all of these 
properties you can choose:
<img src="https://github.com/BoyuanFeng/CS263Project/blob/master/Ant_Properties.png">

#### Selecting a Conﬁguration
A conﬁguration in terms of Jikes RVM is the combination of build time parameters and component selection used for a particular Jikes RVM image. Typical conﬁguration names include:

* **production**: This conﬁguration deﬁnes a fully optimized version of the Jikes RVM.
* **development**: This conﬁguration is the same as production but with debug options enabled. The debug options perform 
internal veriﬁcation of Jikes RVM which means that it builds and executes more slowly.
* **prototype**: This conﬁguration is compiled using an unoptimized compiler and includes minimal components which means it 
has the fastest build time.
* **prototype-opt**: This conﬁguration is compiled using an unoptimized compiler but it includes the adaptive system and optimizing compiler. This conﬁguration has a reasonably fast build time.

#### Fetching Dependencies
The build system will attempt to download and build these dependencies if they are not present or are the wrong version.

#### Building Jikes RVM
The next step in building Jikes RVM is to run the ant command ```ant``` or ```ant -Dconfig.name=....``` This should build a complete RVM runtime in the directory ```${dist.dir}/${config.name}_${target.name}```. A complete list of documented targets can be listed by executing the command ant -projecthelp.

#### Running Jikes RVM
Jikes RVM can be executed in a similar way to most Java Virtual Machines. The diﬀerence is that the command is ```rvm``` and resides in the runtime directory (i.e. ```${dist.dir}/${config.name}_${target.name}```). Detailed command line options can be found [here](http://www.jikesrvm.org/UserGuide/RunningJikesRVM/index.html#x11-1010009).

### Using buildit





