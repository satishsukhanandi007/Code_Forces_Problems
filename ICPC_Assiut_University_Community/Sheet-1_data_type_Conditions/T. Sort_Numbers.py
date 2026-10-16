A, B, C = map(int, input().split())
if A > B:
    if A > C:
        if B > C:
            print(C, B, A, sep = '\n')
        else:
            print(B, C, A, sep = '\n')
    else:
        print(B, A, C, sep = '\n')
else:
    if B > C:
        if A > C:
            print(C, A, B, sep = '\n')
        else:
            print(A, C, B, sep = '\n')
    else:
        print(A, B, C, sep = '\n')
print(f'''
{A}
{B}
{C}''')