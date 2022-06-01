def knapsack(capacity, orders, times):
    DP = [[0 for x in range(capacity + 1)] for x in range(len(total_time) + 1)]

    for i in range(len(total_time) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                DP[i][j] = 0
            elif orders[i-1] > j:
              DP[i][j] = DP[i-1][j]
            else:
              DP[i][j] = max(DP[i-1][j], DP[i-1][j-orders[i-1]] + times[i-1])
    return DP[len(total_time)][capacity]

while True:
  orders = int(input())
  if orders == 0: break
  capacity = int(input())
  total_time = []
  total_pizza = []

  for i in range(orders):
    time, pizzas = [int(x) for x in input().split()]
    total_time.append(time)
    total_pizza.append(pizzas)

  ans = knapsack(capacity, total_pizza, total_time)
  print(ans, 'min.')
