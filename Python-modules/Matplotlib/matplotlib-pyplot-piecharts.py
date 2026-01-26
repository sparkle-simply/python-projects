import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 25, 25, 15])

plt.pie(x)
plt.show()


# adding custom labels and startangle
myLabels = ["Apple", "Banana", "Orange", "Pomegranate"]
plt.pie(x, labels=myLabels, startangle=90)
plt.show()

# adding explode value to make wedge to standout
myExplode = np.array([0.2, 0, 0, 0])
plt.pie(x, labels=myLabels, explode=myExplode)
plt.show()

# adding custom colors to wedges
myColors = np.array(["beige", "yellow", "orange", "red"])
plt.pie(x, labels=myLabels, explode=myExplode, colors=myColors)
plt.show()

# adding legend (list of wedges context) with title
plt.pie(x, labels=myLabels, explode=myExplode, colors=myColors)
plt.legend(title = "Fruits")
plt.show()





