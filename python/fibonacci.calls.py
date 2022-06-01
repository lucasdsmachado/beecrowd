memo = {}
# base cases
# res and calls
memo[1] = [1, 0]
memo[2] = [1, 2]

def fib(n):
  if n in memo: return memo[n]
  else:
    first = fib(n - 1)
    second = fib(n - 2)
    f = [first[0] + second[0], first[1] + second[1] + 2]
  memo[n] = f
  return f

loop = int(input())
for _ in range(loop):
  i = int(input())
  res, calls = fib(i)
  print('fib({}) = {} calls = {}'.format(i, calls, res))
