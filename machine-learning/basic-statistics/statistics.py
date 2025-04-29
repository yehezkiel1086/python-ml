'''
Get the mean, median and mode of the following data:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] 
'''
#!/bin/python

from scipy import stats
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

speed_mean = numpy.mean(speed)
speed_median = numpy.median(speed)
speed_mode, speed_mode_count = stats.mode(speed)

print(f"Mean: {speed_mean}")
print(f"Median: {speed_median}")
print(f"Mode: {speed_mode}, Mode_total: {speed_mode_count}")
