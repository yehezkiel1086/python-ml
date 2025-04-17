#!/bin/python3

import numpy as np

# 0-dimension array
arr0 = np.array(1)
# 1-dimension array
arr1 = np.array([1, 2, 3])
# 2-dimension array
arr2 = np.array([[1, 2, 3], [1, 2, 3]])
# 3-dimension array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# check dimensions
print(np.ndim(arr0))
print(np.ndim(arr1))
print(np.ndim(arr2))
print(np.ndim(arr3))

