# A Survey on HotSpot

## What is Java Virtual Machine (JVM)?
Java is a programming language. To run a Java program, we need to write the source code first, then compile the source code into byte code using "javac". This byte code is a representation of source code in a compact way, which has benefit in transporting through network. To run these byte code, a virtual machine is required. The Java virtual machine is called a virtual machine, since it is a software machine simulating what a real machine does. The Java virtual machine (JVM) has its own instruction set, a virtual computer architecture, and an execution model. With these components, the JVM can do whatever a real machine would do. Based on this virtual machine, Java gains the ability to "write once, run everywhere", since the source code targeting the JVM with same semantic and the JVM will take care of resting work, like how to communicate with real architecture. In other words, JVM becomes the abstract of real architecture and provies a unique API to Java.

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
Previously I installed openJDK. I switched to HotSpot using the following website [4].

## How to run HotSpot



## What are the flags and how to use them




[1] Wikipedia: List of Java virtual machines https://en.wikipedia.org/wiki/List_of_Java_virtual_machines

[2] Wikipedia: HotSpot https://en.wikipedia.org/wiki/HotSpot

[3] http://davisfiore.co.uk/?q=node/255

[4] https://linode.com/docs/development/java/install-java-on-ubuntu-16-04/















