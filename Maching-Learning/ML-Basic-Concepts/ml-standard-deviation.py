import numpy as np

# standard deviation describes how spread out the values are, lower deviation implies more numbers are close to average value and higher deviation implies that values are spread over a wider range

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.std(speed)
print(x)

speed = [32,111,138,28,59,77,97]
x = np.std(speed)
print(x)

