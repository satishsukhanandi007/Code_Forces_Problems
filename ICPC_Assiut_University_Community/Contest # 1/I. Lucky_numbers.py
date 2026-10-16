l,m = map(int, input())

if m == 0:
    print("YES")
elif l % m == 0 or m % l == 0:
    print("YES")
else:
    print("NO")