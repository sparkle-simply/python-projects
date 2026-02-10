import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# train is creating model and test is validating the accuracy of created model

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# training set is 80% of data
train_x = x[:80]
train_y = y[:80]

# testing set is remaining 20% data
test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
myline = numpy.linspace(0, 6, 100)

# using polynomial regression for showing training set relationship
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# getting r2 square value for training set
r2 = r2_score(train_y, mymodel(train_x))
print(r2)

# getting r2 square value for testing set
r2 = r2_score(test_y, mymodel(test_x))
print(r2)

# predicting new values using model when the relationship is 'ok' with fetched r2_square value
print(mymodel(5))