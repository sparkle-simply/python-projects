# It is the table that is used in classification problems to assess where errors in models were made
# The rows represent the actual classes of outcomes that have been made.
# The column represents the predictions we have made.
# Using this table it is easy to see which predictions are made

import numpy
from sklearn import metrics
import matplotlib.pyplot as plt

# setting up actual and predicted values
actual = numpy.random.binomial(1, 0.9, size = 1000)
predicted = numpy.random.binomial(1, 0.9, size = 1000)

# confusion matrix setup
confusion_matrix = metrics.confusion_matrix(actual, predicted)

# confusion matrix visual display
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

# plotting and displaying confusion matrix
cm_display.plot()
plt.show()








