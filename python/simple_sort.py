# -*- coding: utf-8 -*-

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

data = list(map(int, input().split()))
unsorted = data[:]
insertionSort(data)

for value in data:
  print(value)

print("")

for value in unsorted:
  print(value)
