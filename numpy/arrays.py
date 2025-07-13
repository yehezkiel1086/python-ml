#!/bin/python3

import numpy as np

arr = np.array(1) # 0D
arr1 = np.array([1, 2, 3, 4, 5]) # 1D
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 2D
arr3 = np.array([[[4, 5, 6], [7, 8, 9]], [[4, 5, 6], [7, 8, 9]]]) # 3D

print(arr.ndim, arr1.ndim, arr2.ndim, arr3.ndim)
