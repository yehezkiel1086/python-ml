'''
Normal data distribution around 5
'''
#!/bin/python

import matplotlib.pyplot as plt
import numpy

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()
