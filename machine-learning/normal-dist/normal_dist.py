'''
Create a normal data distribution:
- 100000 floats around 5.0 with std deviation of 1.0
  then create the histogram with 100 values division
'''
#!/bin/python

import matplotlib.pyplot as plt
import numpy

arr = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(arr, 100)
plt.show()
