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
A developer can either work with the version control system or download one of the releases. If you are interested in doing 
development of Jikes RVM you should probably use Git instead of downloading a release.
## Download a Release
All the releases can be downloaded at [here](https://sourceforge.net/projects/jikesrvm/files/), you can use your web browser 
to download the latest version of Jikes RVM and uncompress it using the command below:
```
$ tar xvzf jikesrvm-<version>.tar.gz
```
or for the tar-bzip2 archive type:
```
$ tar xvjf jikesrvm-<version>.tar.bz2
```
## Use Git
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
## Detailed Process of Installation of Jikes RVM
<img src="">


