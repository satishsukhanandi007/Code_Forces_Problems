n = int(input())

# while True:

for i in range(1,n+1):
    print(" "*(n-i), "*"*(2*i-1), sep = "")
for i in range(n,0,-1):
    print(" "*(n-i), "*"*(2*i-1), sep = "")

# print(" "*(n), "*")
# print(" "*(n+1), "*")

# for i in range(1,n+1):
#     print(" "*(n-i), "*"*(2*i-1))
# for i in range(n,0,-1):
#     print(" "*(n-i), "*"*(2*i-1))
            # "OR"
# for i in range(1,n+1):
#     print(" "*(n-i+3), "*"*(2*i-1))
# for i in range(n,0,-1):
#     print(" "*(n-i+3), "*"*(2*i-1))

# print(" "*(n+1), "*")
# print(" "*(n), "*")