#!/bin/python

from scipy import stats
import numpy

speeds = [99,86,87,88,111,86,103,87,94,78,77,85,86]

avg = numpy.mean(speeds)
med = numpy.median(speeds)
mode_v, mode_tt = stats.mode(speeds)

print(avg, med, mode_v)
