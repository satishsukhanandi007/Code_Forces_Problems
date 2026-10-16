n = int(input())
for divisor in range(1,n+1):
    if n % divisor == 0:
        # print(divisor)
        print(divisor, end = " ")

# number = 1
# while number <= n:
#     if n % number == 0:
#         print(number)
#     number += 1