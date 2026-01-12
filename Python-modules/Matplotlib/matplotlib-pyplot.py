# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,7])
ypoints = np.array([0,250])


# plotting line between (0,7) and (0, 250), by default plot() function draws line from point to point
plt.plot(xpoints, ypoints)
plt.show()

# plotting markers between (0,7) and (0, 250)
plt.plot(xpoints, ypoints, 'o')
plt.show()

multiple_x_points = np.array([1,2,6,8])
multiple_y_points = np.array([3,8,1,10])

# plotting multiple lines
plt.plot(multiple_x_points, multiple_y_points)
plt.show()

# plotting multiple points with default xpoints
plt.plot(multiple_y_points)
plt.show()