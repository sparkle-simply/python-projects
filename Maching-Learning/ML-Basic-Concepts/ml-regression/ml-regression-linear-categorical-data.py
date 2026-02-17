import pandas
from sklearn import linear_model

cars = pandas.read_csv("data.csv")
# getting numeric representation of the categorical(represented as strings) variable
ohe_cars = pandas.get_dummies(cars[['Car']])

X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X,y)

##predict the CO2 emission of a VW where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])

print(predictedCO2)

# Dummifying

colors = pd.DataFrame({'color': ['blue', 'red']})
print(colors)

dummies = pd.get_dummies(colors, drop_first=True)
print(dummies)

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
dummies['color'] = colors['color']
print(dummies)