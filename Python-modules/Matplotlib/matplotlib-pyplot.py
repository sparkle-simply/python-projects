# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,7])
ypoints = np.array([0,250])

plt.plot(xpoints, ypoints)
plt.show()