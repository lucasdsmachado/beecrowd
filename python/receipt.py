# -*- coding: utf-8 -*-

def maximumSum(list, size):
  curr = 0
  maximum = 0
  for i in range(size):
    curr = max(list[i], curr + list[i])
    maximum = max(maximum, curr)
  return maximum

while True:
  try:
    n = int(input())
    cost = int(input())
    receipts = []
    for _ in range(n):
      receipt = int(input()) - cost
      receipts.append(receipt)
    print(maximumSum(receipts, len(receipts)))
  except EOFError:
    break
