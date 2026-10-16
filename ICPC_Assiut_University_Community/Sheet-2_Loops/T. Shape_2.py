n = int(input())

for i in range(1,n+1):
    print(" "*(n-i), "*"*(2*i - 1), sep = "")
    # print(" "*(n-i), "*"*i, sep = "")
    # print(" "*2*(n-i), "* "*(2*i - 1), sep = "")
    # print(" "*(n-i), "* "*i, sep = "")
