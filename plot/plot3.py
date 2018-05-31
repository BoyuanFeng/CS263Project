import numpy as np
#from basic_units import cm, inch
import matplotlib.pyplot as plt


N = 11
default = (0.831, 1.29, 4.514, 5.235, 7.324, 7.8, 8.913, 12.975, 14.371, 26.258, 116.438)
xbatch = (0.833, 1.31, 4.497, 5.084, 7.963, 7.978, 9.179, 11.773, 14.105, 26.166, 117.066)
aggresive = (0.849, 1.264, 4.378, 4.965, 8.114, 8.066, 9.327, 12.665, 14.52, 26.022, 116.31)
xint = (1.406, 37.663, 118.139, 100.17, 166.427, 9.166, 212.131, 301.266, 193.488, 35, 137)
xcomp = (1.397, 2.361, 8.164, 5.907, 7.61, 9.35, 15.955, 15.122, 14.361, 29.91, 122.762)
xoclassgc = (0.827, 1.28, 4.642, 4.998, 7.19, 7.982, 8.793, 11.721, 13.909, 26.295, 121.159)

fig, ax = plt.subplots()

ind = np.arange(N)    # the x locations for the groups
width = 0.15         # the width of the bars
p1 = ax.bar(ind, default, width, color='r', bottom=0)
p2 = ax.bar(ind + width, xbatch, width, color='y', bottom=0)
p3 = ax.bar(ind + width*2, aggresive, width, color='b', bottom=0)
p4 = ax.bar(ind + width*3, xint, width, color='g', bottom=0)
p5 = ax.bar(ind + width*4, xcomp, width, color='c', bottom=0)
p6 = ax.bar(ind + width*5, xoclassgc, width, color='k', bottom=0)




#ax.set_title('Performance by programs and flags')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('sqrt', 'spectralnorm', 'binarytrees', 'nbody', 'mandelbrot',
                    'pow', 'regexredux', 'knucleotide', 'fannkuchredux',
                    'fasta', 'revcomp'), rotation=45)

ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('Default', 'Xbatch',
              'AggressiveOpts', 'Xint', 'Xcomp', 'Xnoclassgc'))

ax.set_ylabel("Running time (s)")

#ax.yaxis.set_units(inch)
ax.autoscale_view()
plt.subplots_adjust(bottom=0.2)
plt.show()
