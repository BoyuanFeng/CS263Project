## What is Java Virtual Machine (JVM)?
Java is a programming language. To run a Java program, we need to write the source code first, then compile the source code into byte code using "javac". This byte code is a representation of source code in a compact way, which has benefit in transporting through network. To run these byte code, a virtual machine is required. The Java virtual machine is called a virtual machine, since it is a software machine simulating what a real machine does. The Java virtual machine (JVM) has its own instruction set, a virtual computer architecture, and an execution model. With these components, the JVM can do whatever a real machine would do. Based on this virtual machine, Java gains the ability to "write once, run everywhere", since the source code targeting the JVM with same semantic and the JVM will take care of resting work, like how to communicate with real architecture. In other words, JVM becomes the abstract of real architecture and provies a unique API to Java.

## What is HotSpot?
JVM is specified in *the java® virtual machine specification* about the data structure, API, compiling, and so on. Although there is a huge number of specifications, free space still exist on how to implement the JVM. HotSpot is an implementation of the JVM concept, while there is a list of other implementations [1]



[1] Wikipedia: List of Java virtual machines https://en.wikipedia.org/wiki/List_of_Java_virtual_machines


















