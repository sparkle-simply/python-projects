import pandas
from sklearn import linear_model

# multiple regression is linear regression where more than one independent values are used to predict the (dependent) value

# pandas module helps in reading csv files and creating data frame objects
df = pandas.read("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

# filling up regression with data that describes relationship
regr = linear_model.LinearRegression()
regr.fit(X, y)

# predict CO2 emission for car with weight: 2300 and volume: 1300
predictedCO2 = regr.predict([[2300, 1300])
print(predictedCO2)




