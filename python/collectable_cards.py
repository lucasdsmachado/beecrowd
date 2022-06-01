# -*- coding: utf-8 -*-

def gcd(a , b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

loop = int(input())
for _ in range(loop):
  a, b = [int(x) for x in input().split()]
  print(gcd(a, b))
