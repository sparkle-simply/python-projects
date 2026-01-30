import numpy as np

# standard deviation describes how spread out the values are, lower deviation implies more numbers are close to average value and higher deviation implies that values are spread over a wider range

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.std(speed)
print(x)

speed = [32,111,138,28,59,77,97]
x = np.std(speed)
print(x)

""" variance is the opposite and describes how spread the values are
 square root of variance is standard deviation
 square of standard variation is variance

  How to calculate variance:
  1. calculate the mean
  2. get the difference of each record from mean
  3. square the differences
  4. compute the average of squares to get the variance
"""

x = np.var(speed)
print(x)

