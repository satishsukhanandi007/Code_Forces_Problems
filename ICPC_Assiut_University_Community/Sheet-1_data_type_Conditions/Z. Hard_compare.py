A, B, C, D = map(float, input().split())
if A == C and A > 1 and B > D:
    print("YES")
elif A == C:
    print("NO")
elif B == D and A * B > 0 and A > B:
    print("YES")
elif