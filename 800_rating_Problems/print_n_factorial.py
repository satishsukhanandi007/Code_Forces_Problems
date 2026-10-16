n = int(input())
n_factorial = 1
for i in range(2,n+1):
    n_factorial *= i # n_factorial = n_factorial * i
# for i in range(n):
#     n_factorial = n_factorial * (i + 1)
print(n_factorial)