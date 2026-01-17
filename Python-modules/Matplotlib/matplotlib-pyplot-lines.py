# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

ypoints1 = np.array([3,8,1,10])

plt.plot(ypoints1, linestyle = 'dotted')
plt.show()

plt.plot(ypoints1, linestyle = 'dashed', color = 'red', linewidth = 20.5)
plt.show()

ypoints2 = np.array([6,2,7,11])

plt.plot(ypoints1)
plt.plot(ypoints2)

plt.show()



