import numpy
from sklearn import linear_model

# Logistic regression aims to solve classification problems.
# It does this by predicting categorical outcomes, unlike linear regression that predicts a continuous outcome.

# reshaped into column from row for Logistic function to work
# represents cgpa for student
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
# represents whether student able to be topper, 0 for No and 1 for Yes
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# creating logistic regression object
logr = linear_model.LogisticRegression()
# filling the logistic regression object with data to describe the relationship
logr.fit(X,y)

# predicting if student can top with cgpa 3.46
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
print(predicted)

# in logistic regression the coefficient is the expected change in log-odds of having the outcome per unit change in X
log_odds = logr.coef_
odds = numpy.exp(log_odds)
print(odds)

# probability computation for each outcome
def logit2prob(logr,x):
  log_odds = logr.coef_ * x + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)
print(logit2prob(logr, X))