# str1 = input().upper()
# str2 = input().upper()
# print(str1, str2) # if the input are numbers then upper and or lower will not throw any error they simply wont matter for numbers.
# Beginner Level Solutions

k = 0

# for i in range(len(str1)):
#     if str1[i] != str2[i]:
#         if str1[i] > str2[i]:
#             k = 1
#         else:
#             k = -1
#         break
# print(k)


# for i in range(len(str1)):
#     if str1[i] != str2[i]:
#         k = i
#         break
# if str1[k] > str2[k]:
#     k = 1
# elif str1[k] < str2[k]:
#     k = -1
# print(k)


# for i in range(len(str1)):
#     if str1[i] == str2[i]:
#         k = 0
#     elif str1[i] > str2[i]:
#         k = 1
#         break
#     else:
#         k = -1
#         break
# print(k)

# Intermediate Level Solution

# if str1 > str2:
#     print(1)
# elif str1 < str2:
#     print(-1)
# else:
#     print(0)

# Pro Level Solution

# a = input().lower()
# b = input().lower()
# print((a > b) - (a < b))

print(2*True - 9*False, 5*False - 4*True) # True -> 1 and False -> 0