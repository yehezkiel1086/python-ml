'''
create the polynomial regression model
of the following dataset:
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
'''
#!/bin/python

from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy

X = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
Y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

Y_model = numpy.poly1d(numpy.polyfit(X, Y, 3))

Y_line = numpy.linspace(1, 22, 100)

x_predict = int(input("Enter value to predict: "))
y_predict = Y_model(x_predict)

print(f"to Predict: {x_predict} Prediction: {y_predict}")
print(f"R squared score = {r2_score(Y, Y_model(X))}")

plt.scatter(X, Y)
plt.plot(Y_line, Y_model(Y_line))

plt.axvline(x=x_predict, color='orange', linewidth=1)
plt.axhline(y=y_predict, color='orange', linewidth=1)

plt.show()
