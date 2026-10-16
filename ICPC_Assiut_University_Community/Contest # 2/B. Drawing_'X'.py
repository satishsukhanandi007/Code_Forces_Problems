n = int(input())
m = (n+1)//2

for i in range(1,n+1):
    f_l,c = m-1-abs(m-i), 2*abs(m-i)-1
    if i < m:
        print("*"*f_l, "\\", "*"*c, "/", "*"*f_l, sep = "")
    elif i == m:
        print("*"*f_l, "X", "*"*f_l, sep = "")
    else:
        print("*"*f_l, "/", "*"*c, "\\", "*"*f_l, sep = "")