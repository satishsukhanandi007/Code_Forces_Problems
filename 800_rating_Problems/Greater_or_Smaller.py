chr = input()
a, b = map(int, input().split())

def Greater(a,b):
    if a > b:
        return a
    else:
        return b
def Smaller(a,b):
    if a < b:
        return a
    else:
        return b

if chr == "G":
    print(Greater(a,b))
else:
    print(Smaller(a,b))