# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

# with subplot(<number-of-rows>, <number of columns>, <plot-seq>), can draw multiple plots in one figure

# plot1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

# plot2
x = np.array([0,1,2,3])
y = np.array([10, 20, 30, 40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MART")
plt.show()

