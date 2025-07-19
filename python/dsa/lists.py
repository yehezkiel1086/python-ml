#!/bin/python3

def get_lowest(arr):
  lowest = arr[0]
  for x in arr:
    if x < lowest:
      lowest = x
  return lowest

if __name__ == "__main__":
  arr = [9, 12, 7, 4, 11]

  # arr.sort() # to sort ascending

  lowest = get_lowest(arr)

  print(lowest)
