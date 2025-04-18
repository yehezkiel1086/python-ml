#!/bin/python3

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr[0]) # 1d array
print(arr1[1, 0]) # 2d array
print(arr2[1, 0, 1]) # 3d array