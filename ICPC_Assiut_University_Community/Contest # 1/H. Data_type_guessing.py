n, k, a = map(int, input().split())
if n * k % a == 0:
    if n * k // a <= 2147483647:
        print("int")
    else:
        print("long long")
else:
    print("doublen")