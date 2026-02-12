# Reference: https://www.w3schools.com/python/python_ml_confusion_matrix.asp
#
# Overview:
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

# The Confusion Matrix created has four different quadrants:
#
# True Negative (Top-Left Quadrant)
# False Positive (Top-Right Quadrant)
# False Negative (Bottom-Left Quadrant)
# True Positive (Bottom-Right Quadrant)
#
# The matrix provides us with many useful metrics that help us to evaluate our classification model.
#
# The different measures include: Accuracy, Precision, Sensitivity (Recall), Specificity, and the F-score.

# Accuracy measures how often the model is correct.
# (True Positive + True Negative) / Total Predictions
Accuracy = metrics.accuracy_score(actual, predicted)

# Of the positives predicted, what percentage is truly positive
# True Positive / (True Positive + False Positive)
Precision = metrics.precision_score(actual, predicted)

# Of all the positive cases, what percentage are predicted positive
# True Positive / (True Positive + False Negative)
Sensitivity_recall = metrics.recall_score(actual, predicted)

# How well the model is at prediciting negative results
# True Negative / (True Negative + False Positive)
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

# F-score is the "harmonic mean" of precision and sensitivity.
# 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
F1_score = metrics.f1_score(actual, predicted)

# metrics
print({"Accuracy":Accuracy,"Precision":Precision,"Sensitivity_recall":Sensitivity_recall,"Specificity":Specificity,"F1_score":F1_score})









