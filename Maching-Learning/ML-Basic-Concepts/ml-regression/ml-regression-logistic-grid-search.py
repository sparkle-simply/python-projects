from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# Grid Search:
# The majority of machine learning models contain parameters that can be adjusted to vary how the model learns.
# How do we pick the best value for this parameter, the best value is dependent on the data used to train the model.
# One method is to try out different values and then pick the value that gives the best score. This technique is known as a grid search.
# If we had to select the values for two or more parameters, we would evaluate all combinations of the sets of values thus forming a grid of values.
# Higher values of parameter tell the model, the training data resembles real world information, place a greater weight on the training data. While lower values do the opposite.

# load in the data set
iris = datasets.load_iris()

# fetching set of independent variables (X) and dependent variable (Y)
X = iris['data']
y = iris['target']

# creating the model, setting max_iter to a higher value to ensure that the model finds a result
logit = LogisticRegression(max_iter = 10000)

# fit the model to the data with default value of c as 1
print(logit.fit(X,y))

# evaluating accuracy of model
print(logit.score(X,y))

# implementing grid search with setting a range of values for C
C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
scores = []

for choice in C:
  logit.set_params(C=choice)
  logit.fit(X, y)
  scores.append(logit.score(X, y))

# We can see that the lower values of C performed worse than the base parameter of 1.
# However, as we increased the value of C to 1.75 the model experienced increased accuracy.
# Also, increasing C beyond one amount (example 1.75) does not help increase model accuracy.
print(scores)
