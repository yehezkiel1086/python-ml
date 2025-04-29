'''
- generate random number
- 
'''
#!/bin/python

import matplotlib.pyplot as plt
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)
y = numpy.random.uniform(0.0, 5.0, 100000)

# print(x)

# plt.hist(x, 5)
# plt.show()
plt.hist(y, 100)
plt.show()
