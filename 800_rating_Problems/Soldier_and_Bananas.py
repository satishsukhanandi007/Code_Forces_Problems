k, n, w = map(int, input().split())
required_n = k*w*(w+1)//2

if required_n > n:
    print(required_n - n)
else:
    print(0)
