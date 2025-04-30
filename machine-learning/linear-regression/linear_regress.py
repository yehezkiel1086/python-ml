'''
- Draw the linear regression line of the following dataset:
  X = [5,7,8,7,2,17,2,9,4,11,12,9,6]
  Y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
- Predict the speed of a 10 years old car
'''
#!/bin/python

from scipy import stats
import matplotlib.pyplot as plt

X = [5,7,8,7,2,17,2,9,4,11,12,9,6]
Y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(X, Y)

def linear_func(x):
  return x * slope + intercept

Y_model = list(map(linear_func, X))

plt.scatter(X, Y)
plt.plot(X, Y_model)
plt.show()

print(f"Value of 10 years old car: {linear_func(10)}")
