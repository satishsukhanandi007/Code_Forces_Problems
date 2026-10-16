A, B, C = map(int, input().split())
if A > B:
    if A > C:
        if B > C:
            print(C, A)
        else:
            print(B, A)
    else:
        print(B, C)
else:
    if B > C:
        if A > C:
            print(C, B)
        else:
            print(A, B)
    else:
        print(A, C)