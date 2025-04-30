'''
- Draw the linear regression line of the following dataset:
  X = [5,7,8,7,2,17,2,9,4,11,12,9,6]
  Y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
- Predict the speed of a 10 years old car
'''
#!/bin/python

from scipy import stats
import matplotlib.pyplot as plt

X = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
Y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

slope, intercept, r, p, std_err = stats.linregress(X, Y)

def linear_func(x):
  return x * slope + intercept

Y_model = list(map(linear_func, X))

x_predict = int(input("Enter value to predict: "))
y_predict = linear_func(x_predict)

print(f"to predict: {x_predict}, prediction: {y_predict}")
print(f"R score = {r}")

plt.scatter(X, Y)
plt.plot(X, Y_model)

plt.axvline(x=x_predict, color='orange', linewidth=1)
plt.axhline(y=y_predict, color='orange', linewidth=1)

plt.show()
