import matplotlib.pyplot as plt
import numpy as np

# with bar utility, bar graph layout is plotted with category and corresponding values as first and second argument
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()

# horizontal bar graph plot
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

# bar graph plotting with custom color and width
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="#4CAF50", width=0.2) # by default width is 0.8
plt.show()

# horizontal bar graph plotting with custom color and height
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, color="#4CAF50", height=0.2) # by default height is 0.8
plt.show()
