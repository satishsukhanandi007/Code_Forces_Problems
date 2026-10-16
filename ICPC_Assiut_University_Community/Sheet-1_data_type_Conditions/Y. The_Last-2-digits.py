A, B, C, D = map(int, input().split())
p = A*B*C*D%100
if p == 0:
    print("00")
elif p < 10:
    print(f"0{p}")
else:
    print(p)