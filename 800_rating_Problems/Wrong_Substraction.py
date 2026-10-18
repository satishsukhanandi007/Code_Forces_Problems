n, k = map(int, input().split())
m = n
for _ in range(k):
    if m % 10 == 0:
        m //= 10
    else:
        m -= 1
print(m)