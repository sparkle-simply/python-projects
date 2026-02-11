import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

# Scaling is standardizing values that are easy to compare for predicting outcome
df = pandas.read("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

# Formula: z = (x - u)/s. Here z is new value, x is existing value, u is mean and s is standard deviation
scaledX = scale.fit_transform(X)
print(scaledX)

regr = linear_model.Linear_Regression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0])
print(predictedCO2)
