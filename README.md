# Performance Comparisons
We are going to compare the performance of PyPy, IronPython, JIT, and CPython. The
comparison will focus on running time, memory usage, and CPU usage. First we will collect 10
programs from website (​ http://benchmarksgame.alioth.debian.org​ ) and try to run them on all
of four platforms. Second step is to summary the running time, memory usage, and CPU usage
in a table or graph to get an intuitive result. Once we notice some pattern, we will investigate the
difference between these platforms based on our observations and give reasons about the
performance difference, stressing the trade-off and design choice. Finally, we will give a
summary of pros and cons for each interpreter on different tasks, which could guide our
interpreter choice in the future.
