import numpy as np
import matplotlib.pyplot as plt

# uniform data distribution uniform(low, high, values to be generated)
x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 5)
plt.show()

# normal data distribution normal(mean, standard deviation, values to be generated)
x = np.random.uniform(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

# random distribution with scatter view
x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()