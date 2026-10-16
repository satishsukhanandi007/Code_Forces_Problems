a, s, b = input().split()
a, b = int(a), int(b)
if s == '<':
    if a < b:
        print("Right")
    else:
        print("Wrong")
elif s == '>':
    if a > b:
        print("Right")
    else:
        print("Wrong")
else:
    if a == b:
        print("Right")
    else:
        print("Wrong")