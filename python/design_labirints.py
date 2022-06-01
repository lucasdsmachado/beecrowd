n = int(input())
pairs = set()
for i in range(n):
  t = int(input())
  v, a = [int(x) for x in input().split()]
  for j in range(a):
    begin, end = input().split()
    pairs.add(begin+end)
    pairs.add(end+begin)
  print(len(pairs))
  pairs = set()
