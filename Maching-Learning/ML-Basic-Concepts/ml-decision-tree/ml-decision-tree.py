import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Decision tree is a flow chart that helps in making decisions based on previous experiences

df = pandas.read_csv("data.csv")
print(df)

# to make decision tree, we need to convert all data to numerical
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
print(df)

# features are values use to predict and target are values that we try to predict
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
print(X)
print(y)

# creating decision tree
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# plotting decision tree
tree.plot_tree(dtree, feature_names=features)

# predicting target based on provided feature values, this is dependent on probability of outcome and result may vary for same ingested data
print(dtree.predict([[40, 10, 7, 1]]))
print(dtree.predict([[40, 10, 6, 1]]))

