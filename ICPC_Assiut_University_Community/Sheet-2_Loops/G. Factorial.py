n= int(input())
n_factorial = 1

# Using while loop

while n > 0:
    m = int(input())
    n_factorial = 1
    n -= 1
    while m > 0:
        n_factorial *= m
        m -= 1
    print(n_factorial)

# Using for loop

# for i in range(n):
#     number = int(input())
#     n_factorial = 1
#     for j in range(2,number+1):
#         n_factorial *= j
#     print(n_factorial)