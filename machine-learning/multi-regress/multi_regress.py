'''
given the cars_dataset.csv dataset:
predict the value of CO2 given:
  - Weight = 2300kg
  - Volume = 1300cm3
'''
#!/bin/python

from sklearn import linear_model
import pandas

df = pandas.read_csv("cars_dataset.csv")

X = df[["Weight", "Volume"]]
y = df["CO2"]

regress = linear_model.LinearRegression()
regress.fit(X, y)

print(regress.coef_)

predicted = regress.predict([[2300, 1300]])

print(predicted)
