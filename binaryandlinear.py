import math

def linear_search(arr, num):
  for i in range(len(arr)):
    if(arr[i] == num):
      return i
    
  return -1

def binary_search(arr, num):
  start = 0
  end = len(arr) - 1
  mid = math.floor((start + end) / 2)

  while(arr[mid] != num):
    if num < arr[mid]:
      end = mid - 1
    else:
      start = mid + 1
    mid = math.floor((start + end) / 2)

  if arr[mid] == num:
    return mid
  return -1



print(linear_search([1, 2, 3], 2))
print(binary_search([1, 2, 3, 4, 5], 3))