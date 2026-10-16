A, B = map(int, input().split())

while True:

    if A > B:
        A = A - (A//B)*B
    else:
        B = B - (B//A)*A

    if A == 0:
        print(B)
        break
    elif B == 0:
        print(A)
        break