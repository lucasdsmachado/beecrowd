# -*- coding: utf-8 -*-

def dfs(matrix, i, j):
  visited[i][j] = True
  if (j + 1 < 5 and visited[i][j + 1] == False and matrix[i][j + 1] == 0):
    dfs(matrix, i, j + 1)
  if (j - 1 >= 0 and visited[i][j - 1] == False and matrix[i][j - 1] == 0):
    dfs(matrix, i, j - 1)
  if (i + 1 < 5 and visited[i + 1][j] == False and matrix[i + 1][j] == 0):
    dfs(matrix, i + 1, j)
  if (i - 1 >= 0 and visited[i - 1][j] == False and matrix[i - 1][j] == 0):
    dfs(matrix, i - 1, j)

n = int(input())
for _ in range(n):
  visited = [[False for _ in range(5)] for _ in range(5)]
  M = []
  i = 0
  while i < 5:
    temp = input().split()
    if temp:
      M.append(list(map(int, temp)))
      i += 1

  dfs(M, 0, 0)
  if (visited[4][4] and M[0][0] != 1):
    print('COPS')
  else:
    print('ROBBERS')
