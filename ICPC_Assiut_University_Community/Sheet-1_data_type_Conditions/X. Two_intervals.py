a, b, c, d = map(int, input()    . split     (   ) )
lower = max(a, c)
upper = min(b, d)
if upper - lower >= 0:
    print(lower, upper)
else:
    print(-1)