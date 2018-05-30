import matplotlib.pyplot as plt

y = [24.259, 96.614, 13.766, 1.377, 4.938, 4.43, 7.363, 8.655, 11.802, 0.823, 7.69]
y.sort()
x = range(11)
plt.bar(x,y)
#plt.plot(x)
plt.xlabel("Programs")
plt.ylabel("Seconds")
plt.title("Overview on performance of selected programs")
plt.show()
