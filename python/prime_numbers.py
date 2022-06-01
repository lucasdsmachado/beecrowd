import math
n = float(input())
p = n/math.log(n, math.e)
m = (n/math.log(n, math.e)) * 1.25506
print("{:.1f} {:.1f}".format(p, m))
