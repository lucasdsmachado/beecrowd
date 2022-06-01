def factorial(num, k):
  ans = num
  i = 1
  while num - (k * i) >= 1:
    ans *= (n - (k * i))
    i += 1
  return ans

loop = int(input())
for _ in range(loop):
  str = input()
  k = str.count('!')
  n = int(str.strip('!'))
  print(factorial(n, k))
