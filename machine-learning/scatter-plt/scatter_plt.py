'''
- Create scatter plot for the following datasets:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
- Let us create two arrays that are both filled with 1000 
random numbers from a normal data distribution.
  The first array will have the mean set to 5.0 with a standard deviation of 1.0.
  The second array will have the mean set to 10.0 with a standard deviation of 2.0:
'''
#!/bin/python

import matplotlib.pyplot as plt
import numpy

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

X = numpy.random.normal(5.0, 1.0, 1000)
Y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(X, Y)
plt.show()
