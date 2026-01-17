# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np


multiple_y_points = np.array([3,8,1,10])


# plotting with markers
plt.plot(multiple_y_points, marker = 'D')
plt.show()

# plotting markers with shortcut notation, marker|line|color
plt.plot(multiple_y_points, 'o:r')
plt.show()

# plotting markers with marker size, ms
plt.plot(multiple_y_points, marker = 'o', ms = 20)
plt.show()

# plotting markers with marker edge color, mec
plt.plot(multiple_y_points, marker = 'o', ms = 20, mec = 'r')
plt.show()

# plotting markers with marker face color, mfc
plt.plot(multiple_y_points, marker = 'o', ms = 20, mec = 'c')
plt.show()

# plotting markers with both mec and mfc
plt.plot(multiple_y_points, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()