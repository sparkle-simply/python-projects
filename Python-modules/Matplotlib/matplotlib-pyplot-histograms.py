import matplotlib.pyplot as plt
import numpy as np

# histogram is used for plotting frequency distribution within intervals
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()