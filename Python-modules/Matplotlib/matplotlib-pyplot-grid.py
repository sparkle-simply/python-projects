# Most of the matplotlib utilities lie under pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([200, 210, 220, 230, 240, 245, 250, 260, 270, 280])

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'red', 'size': 15}

plt.title("Health Analytics", fontdict = font1, loc = 'left')
plt.xlabel("Average pulse", fontdict = font2)
plt.ylabel("Coloriee burnage", fontdict = font2)

plt.plot(x, y)

# by default both x, y axis are displayed
plt.grid()
plt.show()

plt.plot(x, y)
plt.grid(axis = 'x')
plt.show()

plt.plot(x, y)
plt.grid(axis = 'y')
plt.show()

plt.plot(x, y)
plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)
plt.show()