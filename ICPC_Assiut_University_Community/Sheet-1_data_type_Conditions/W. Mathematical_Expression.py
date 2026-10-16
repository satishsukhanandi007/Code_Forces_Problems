A, S, B, Q, C = input().split()
A, B, C = int(A), int(B), int(C)
if S == "+" and A + B == C:
    print("Yes")
elif S == "+":
    print(A + B)
elif S == "-" and A - B == C:
    print("Yes")
elif S == "-":
    print(A - B)
elif S == "*" and A * B == C:
    print("Yes")
else:
    print(A * B)