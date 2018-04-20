# A Survey on HotSpot

## What is Java Virtual Machine (JVM)?
Java is a programming language. To run a Java program, we need to write the source code first, then compile the source code into byte code using "javac". This byte code is a representation of source code in a compact way, which has benefit in transporting through network. To run these byte code, a virtual machine is required. The Java virtual machine is called a virtual machine, since it is a software machine simulating what a real machine does. The Java virtual machine (JVM) has its own instruction set, a virtual computer architecture, and an execution model. With these components, the JVM can do whatever a real machine would do. Based on this virtual machine, Java gains the ability to "write once, run everywhere", since the source code targeting the JVM with same semantic and the JVM will take care of resting work, like how to communicate with real architecture. In other words, JVM becomes the abstract of real architecture and provies a unique API to Java.

## What is JRE? What is the difference between JRE and JVM?
According to stackoverflow [5], JRE stands for *Java Runtime Environment*, which includes Java Virtual Machine (JVM), class libraries, and other supporting files. JRE does not contain any development tools such as compiler, debugger, etc. JVM makes use of class libraries and other supporting files provided in JRE to actually run the program. So JVM is a component of JRE.

## What is HotSpot?
JVM is specified in *the java® virtual machine specification* about the data structure, API, compiling, and so on. Although there is a huge number of specifications, free space still exist on how to implement the JVM. HotSpot is an implementation of the JVM concept, while there is a list of other implementations [1]. According to wikipedia [2], there are a few important points about HotSpot that we should know. Italic sentence are copied directly from wikipedia and other sentence are summarized and rephrased by myself.
* *HotSpot, released as Java HotSpot Performance Engine, is a Java virtual machine for desktop and server computers, maintained and distributed by Oracle Corporation. The Java HotSpot Performance Engine was first released April 27, 1999.*
* *Hotpot improved performance via methods such as just-in-time compilation and adaptive optimization.*
* *HotSpot is written in C++. In 2007, Sun estimated it comprised approximately 250,000 lines of source code.*
* *HotSpot supports many command-line arguments for options of the virtual machine execution. Some are standard and must be found in any conforming Java virtual machine; others are specific to HotSpot and may not be found in other JVMs (options that begin with -X or -XX are non-standard).*

In summary, HotSpot is an implementation of JVM. There are lots of command-line argument, which may have various influence on the performance. The main point of our project is to try these arguments, record the influence on performance, and understand the reason behind scene.

## What is OpenJDK
JDK stands for *Java Development Kit*. According to website [3], OpenJDK is another important implementation of Java, since it is the reference implementation: *Both "Java Language Specification" and "Java Virtual Machine Specifications" are freely available. There are multiple JDK and virtual machine implementations, some open source and others commercial. HotSpot is the most popular virtual machine, distributed with Oracle JDK. This is a commercial distribution and is pretty stable. However OpenJdk, initially developed by Sun Microsystems, is still the reference implementation, under GPL license.* 

In our project, we will first try to use HotSpot. Then we will also run the same experiments on OpenJDK and compare the performance with HotSpot.


## How to install HotSpot
Previously I installed openJDK. I switched to HotSpot following the instructions from website [4].

## How to run HotSpot
HotSpot is an implementation of JVM. On how to run HotSpot, there is not too much difference between HotSpot and other implementations. Simply type *java xxx* is enough.


## What are the flags and how to use them
Oracle Java document [6] gives a nice explanation of what the flag are and how to use them. 
```
java [options] classname [args]
```

* options: Command-line options separated by spaces
* classname: The name of the class to be launched.
* args: The arguments passed to the main() method separated by spaces.

The following list presents a subset of options which are interesting for the author. These options are interesting since they may have tremendous impact on the performance. All of descriptions are copied from Oracle Java Document [6] directly.

* -d32: Run program in 32-bit mode
* -d64: Run program in 64-bit mode
* -Xbatch: Disables background compilation. By default, the JVM compiles the method as a background task, running the method in interpreter mode until the background compilation is finished. The -Xbatch flag disables background compilation so that compilation of all methods proceeds as a foreground task until completed.
* -Xcomp: Forces compilation of methods on first invocation. By default, the Client VM (-client) performs 1,000 interpreted method invocations and the Server VM (-server) performs 10,000 interpreted method invocations to gather information for efficient compilation. Specifying the -Xcomp option disables interpreted method invocations to increase compilation performance at the expense of efficiency.
* -Xint: Runs the application in interpreted-only mode. Compilation to native code is disabled, and all bytecode is executed by the interpreter. The performance benefits offered by the just in time (JIT) compiler are not present in this mode.
* -Xmixed: Executes all bytecode by the interpreter except for hot methods, which are compiled to native code.
* -Xnoclassgc: Disables garbage collection (GC) of classes. This can save some GC time, which shortens interruptions during the application run.
* -XX:+AggressiveOpts: Enables the use of aggressive performance optimization features.
* -XX:+AggressiveHeap: Enables Java heap optimization. This sets various parameters to be optimal for long-running jobs with intensive memory allocation, based on the configuration of the computer (RAM and CPU). By default, the option is disabled and the heap is not optimized.
* -XX:NativeMemoryTracking=mode: Specifies the mode for tracking JVM native memory usage.


## Plan for next week
Collect a set of interesting programs and run these program using HotSpot.


[1] Wikipedia: List of Java virtual machines https://en.wikipedia.org/wiki/List_of_Java_virtual_machines

[2] Wikipedia: HotSpot https://en.wikipedia.org/wiki/HotSpot

[3] http://davisfiore.co.uk/?q=node/255

[4] https://linode.com/docs/development/java/install-java-on-ubuntu-16-04/

[5] Stack Overflow: What is the difference between the JRE and JVM? https://stackoverflow.com/questions/2812549/what-is-the-difference-between-the-jre-and-jvm

[6] Oracle Java Document: Java https://docs.oracle.com/javase/8/docs/technotes/tools/unix/java.html












