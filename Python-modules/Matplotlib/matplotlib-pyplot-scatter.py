# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

# scatter plots dot for each observation

# plot1
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y, c="pink")

# plot2
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y, c="green")

# by default blue and orange color get plotted with scatter of 2 plots
plt.show()


# with scatter, we can plot each dots with different colors using colors array
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()


# using colormap, matplot module has number of available colormaps
# color map is list of color, with each color having values that ranges from 0 to 100
x = np.array([5,7,8,7,2,17,2,9,4,11])
y = np.array([99,86,87,88,111,86,103,87,94,78])
colors = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap="viridis") # viridis is one of inbuilt colormap

plt.colorbar() # including colormap visibility

plt.show()

# defining size for each plotted dot using "s" attribute and transparency of dots using "alpha" attribute
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

# combining all scatter properties for visibility and usage


x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap="nipy_spectral")

plt.colorbar()

plt.show()

