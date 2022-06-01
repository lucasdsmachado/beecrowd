# -*- coding: utf-8 -*-
from math import ceil

def gambler(n1, n2, d):
  if d == 3:
    return n1/(n1 + n2) * 100
  else:
    p = 1 - (6 - d)/6
    p = (1 - p)/p
    return (1 - pow(p, n1))/(1 - pow(p, n1+n2)) * 100

while True:
  n1, n2, at, dmg = [int(x) for x in input().split()]
  if n2 == n2 == at == dmg == 0:
    break
  n1, n2 = ceil(n1/dmg), ceil(n2/dmg)
  ans = gambler(n1, n2, at)
  print('{:.1f}'.format(ans))
