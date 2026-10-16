A, B = map(int, input().split())

if  A%B == 0:
    ceil = A//B
else:
    ceil = A//B + 1

if A%B == B/2:
# if A/B - A//B == .5:
    round = A//B + 1
else:
    round = round(A/B)

print(f'''floor {A} / {B} = {A//B}
ceil {A} / {B} = {ceil}
round {A} / {B} = {round}''')
