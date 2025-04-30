'''
Generate uniform random numbers:
250 random floats from 0.0 to 5.0
  then show the histogram divided by 5 datas
100000 random floats from 0.0 to 5.0
  then show the histogram divided by 100 datas
'''
#!/bin/python

import matplotlib.pyplot as plt
import numpy

r_1 = numpy.random.uniform(0.0, 5.0, 250)
r_2 = numpy.random.uniform(0.0, 5.0, 100000)

# print(r_1)

# plt.hist(r_1, 5)
plt.hist(r_2, 100)
plt.show()
