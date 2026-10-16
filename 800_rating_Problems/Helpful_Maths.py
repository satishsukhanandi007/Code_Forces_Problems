summan = list(map(int, input().split("+")))
a = 0
b = 0
c = 0
for i in summan:
    if i == 1:
        a += 1
    elif i == 2:
        b += 1
    else:
        c += 1
if a > 0:
    if b == 0 and c == 0:
        print("1+"*(a-1), "1", sep = "")
    else:
        print("1+"*(a-1), "1", end = "+" ,sep = "")
if b > 0:
    if c == 0:
        print("2+"*(b-1), "2", sep = "")
    else:
        print("2+"*(b-1), "2", end = "+" ,sep = "")
if c > 0:
        print("3+"*(c-1), "3", sep = "")
    