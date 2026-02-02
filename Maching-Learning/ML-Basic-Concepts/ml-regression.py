import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# key values from line regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

def computeY(x):
    return x * slope + intercept

# mapping based on line regression
customModel = list(map(computeY(x), x)

plt.scatter(x, y)
plt.plot(x, computeY)
plt.show()

# prediction car speed that is 10 years old now
print(computeY(10))