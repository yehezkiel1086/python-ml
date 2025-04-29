'''
standard deviation, variance
'''
#!/bin/python

import numpy

speeds_1 = [86,87,88,86,87,85,86]
speeds_2 = [32,111,138,28,59,77,97]

std_dev_1 = numpy.std(speeds_1)
var_1 = numpy.var(speeds_1)
std_dev_2 = numpy.std(speeds_2)
var_2 = numpy.var(speeds_2)

print(std_dev_1, std_dev_2)
print(var_1, var_2)
