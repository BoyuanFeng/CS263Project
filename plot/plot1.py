import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import pandas as pd

height1 = [26.258, 26.924, 29.852, 28.823, 27.07, 28.011, 28.231, 27.97, 28.704, 27.57]
SR_y = pd.Series(height1, name="fasta")
fig, (ax1, ax2) = plt.subplots(1,2)
sns.distplot(SR_y, bins=5, color="g", ax=ax1)

height2 = [1.392, 1.522, 1.577, 1.572, 1.52, 1.472, 1.452, 1.475, 1.424, 1.368]
SR_y = pd.Series(height2, name="spectralnorm")
sns.distplot(SR_y, bins=5, color="g", ax=ax2)

fig.suptitle('Performance of two selected programs') 
#x = range(10)
#plt.bar(x, height)
plt.show()
