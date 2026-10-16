X = int(input())

prime = 0
for i in range(2,X):
    if X % i != 0:
        prime += 1
    else:
        break
if prime == X-2:
    print("YES")
elif X == 1:
    print("NO")

# if X == 1:
#     print("NO")
# n = X-1       # division till 2
# prime = 0
# while n > 1:
#     if X % n != 0:
#         prime += 1
#     else:
#         print("NO")
#         break
#     n -= 1
# if prime == X-2:
#     print("YES")


# if X == 1:
#     print("NO")
# n = 2
# prime = 0
# while n < X:
#     if X % n != 0:
#         prime += 1
#     else:
#         print("NO")
#         break
#     n += 1
# if prime == X-2:
#     print("YES")