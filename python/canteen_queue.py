# -*- coding: utf-8 -*-

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

loop = int(input())

for _ in range(loop):
  count = 0
  size = int(input())
  unsortedArray = list(map(int, input().split()))
  sortedArray = unsortedArray[:]
  insertionSort(sortedArray)
  for i in range(size):
    if unsortedArray[i] == sortedArray[i]:
      count += 1
  print(count)
