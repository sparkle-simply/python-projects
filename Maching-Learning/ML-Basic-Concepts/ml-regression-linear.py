import matplotlib.pyplot as plt
import numpy as np

# polynomial regression plots line passing through data points in best way possible using their relationship

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# building custom polynomial model
customModel = np.ploy1d(np.polyfit(x, y, 3))
# defining about line visibility from 1 to 22 position
customLine = np.linespace(1, 22, 100)

# original scatter plot
plt.scatter(x, y)
# polynomial regression
plt.plot(customLine, customModel)
# displaying diagram
plt.show()