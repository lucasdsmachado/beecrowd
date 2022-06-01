x1, y1 = [float(i) for i in input().split()]
x2, y2 = [float(j) for j in input().split()]
ans = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("{:.4f}".format(ans))
