'''
Find the standard deviation and variance of the following datas:
speed_1 = [86,87,88,86,87,85,86]
speed_2 = [32,111,138,28,59,77,97] 
'''
#!/bin/python

import numpy

speed_1 = [86,87,88,86,87,85,86]
speed_2 = [32,111,138,28,59,77,97]

dev_1 = numpy.std(speed_1)
dev_2 = numpy.std(speed_2)

var_1 = numpy.var(speed_1)
var_2 = numpy.var(speed_2)

print(f"Standard deviation 1: {dev_1}")
print(f"Standard deviation 2: {dev_2}")

print(f"Variance 1: {var_1}")
print(f"Variance 2: {var_2}")
