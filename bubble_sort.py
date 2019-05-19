# -*- coding: utf-8 -*-
"""bubble_sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b1QlJ4dKuDSW2BJiaUjz-7Wg_gupnIED
"""

def bubble_sort(array, n):
  for i in range(1, n):
    for j in range(1, n-i + 1):
      if array[j-1] > array[j]:
        temp = array[j] 
        array[j] = array[j-1]
        array[j-1] = temp
  return array

array = [6, 5, 3, 1, 9, 7, 2, 4, 8]
array = bubble_sort(array, len(array))
print(array)