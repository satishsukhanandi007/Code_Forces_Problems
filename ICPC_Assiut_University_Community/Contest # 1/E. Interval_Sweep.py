a, b = map(int, input().split())
if a == b == 0:
    print("NO")
elif a == b + 1 or b == a + 1 or a == b:
    print("YES")
else:
    print("NO")