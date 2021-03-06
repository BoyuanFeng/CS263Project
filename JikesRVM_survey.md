# 1. What is Jikes RVM
Jikes RVM is a virtual machine that runs Java programs. Unlike most other JVMs, it is written in Java, a style of
implementation termed meta-circular. Jikes RVM runs on many platforms. These platforms includes IA-32 Linux and PowerPC 64
Linux which are well supported and OS X, Solaris and PowerPC 32 which are less well-supported. It advances the state-of-the-
art of virtual machine technologies for dynamic compilation, adaptive optimization, garbage collection, thread scheduling, and 
synchronization. A distinguishing characteristic of Jikes RVM is that it is implemented in the Java™ programming language and 
is self-hosted i.e., its Java code runs on itself without requiring a second virtual machine. Most other virtual machines for 
the Java platform are written in native code (typically, C or C++). A Java implementation provides ease of portability, and a 
seamless integration of virtual machine and application resources such as objects, threads, and operating-system interfaces.

# 2. How to Install Jikes RVM
## 2.1 Get the Source
A developer can either work with the version control system or download one of the releases. If you are interested in doing 
development of Jikes RVM you should probably use Git instead of downloading a release.

### 2.1.1 Download a Release
All the releases can be downloaded at [here](https://sourceforge.net/projects/jikesrvm/files/), you can use your web browser 
to download the latest version of Jikes RVM and uncompress it using the command below:
```
$ tar xvzf jikesrvm-<version>.tar.gz
```
or for the tar-bzip2 archive type:
```
$ tar xvjf jikesrvm-<version>.tar.bz2
```

### 2.1.2 Use Git
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

### 2.1.3 Detailed Process
<img src="https://github.com/BoyuanFeng/CS263Project/blob/master/Installation_JikesRVM.png">

## 2.2 Building Jikes RVM
Once you’ve met the requisite dependencies you can use the buildit script to build the system faster and easier. To avoid 
problems with the build, make sure that the path to the Jikes RVM source code doesn’t contain any whitespace.

### 2.2.1 Target Requirements
Note that x86_64 is currently only supported using the legacy 32bit addressing mode and instructions. You need to install the 
32-bit versions of the required libraries to build and use the x86_64 conﬁgurations.

### 2.2.2 Tool Requirements

Java Virtual Machine, Ant, C compilers, Bison, Perl, Awk.

### 2.2.3 Building Process

#### 2.2.3.1 Deﬁning Ant Properties
There are lots of ant properties you can configure for the build process of Jikes RVM, Figure below shows the all of these 
properties you can choose:
<img src="https://github.com/BoyuanFeng/CS263Project/blob/master/Ant_Properties.png">

#### 2.2.3.2 Selecting a Conﬁguration
A conﬁguration in terms of Jikes RVM is the combination of build time parameters and component selection used for a particular Jikes RVM image. Typical conﬁguration names include:

* **production**: This conﬁguration deﬁnes a fully optimized version of the Jikes RVM.
* **development**: This conﬁguration is the same as production but with debug options enabled. The debug options perform 
internal veriﬁcation of Jikes RVM which means that it builds and executes more slowly.
* **prototype**: This conﬁguration is compiled using an unoptimized compiler and includes minimal components which means it 
has the fastest build time.
* **prototype-opt**: This conﬁguration is compiled using an unoptimized compiler but it includes the adaptive system and optimizing compiler. This conﬁguration has a reasonably fast build time.

#### 2.2.3.3 Fetching Dependencies
The build system will attempt to download and build these dependencies if they are not present or are the wrong version.

#### 2.2.3.4 Building Jikes RVM
The next step in building Jikes RVM is to run the ant command ```ant``` or ```ant -Dconfig.name=....``` This should build a complete RVM runtime in the directory ```${dist.dir}/${config.name}_${target.name}```. A complete list of documented targets can be listed by executing the command ```ant -projecthelp```.

#### 2.2.3.5 Running Jikes RVM
Jikes RVM can be executed in a similar way to most Java Virtual Machines. The diﬀerence is that the command is ```rvm``` and resides in the runtime directory (i.e. ```${dist.dir}/${config.name}_${target.name}```). Detailed command line options can be found [here](http://www.jikesrvm.org/UserGuide/RunningJikesRVM/index.html#x11-1010009).

### 2.2.4 Using buildit

buildit script is an easier way to build and test the system, and it contains lots of options, you can take a look at the options by running
```
bin/buildit -h
```
# 3 Plan for Next Week

Start to test some [programs](https://benchmarksgame-team.pages.debian.net/benchmarksgame/) and measure the performances like time consumption, memory usage, and CPU usage on Jikes RVM.

# 4 Acknowledgement

Thanks to the official guide on Jikes RVM [website](http://www.jikesrvm.org/), most of instructions here are learned from 
there.


