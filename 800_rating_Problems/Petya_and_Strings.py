str1 = input().upper()
str2 = input().upper()
# print(str1, str2) # if the input are numbers then upper and or lower will not throw any error they simply wont matter for numbers.

if str1 > str2:
    print(1)
elif str1 < str2:
    print(-1)
else:
    print(0)


# The Process
# for i in range(len(str1)):
#     if str1[i] != str2[i]:
#         if str1[i] > str2[i]:
#             print(1)
#         else:
#             print(-1)
#         break



# for i in range(len(str1)):
#     if str1[i] != str2[i]:
#         break
# if str1[i] > str2[i]:
#     print(1)
# else:
#     print(-1)
# print(k)


# for i in range(len(str1)):
#     if str1[i] == str2[i]:
#         print(0)
#     elif str1[i] > str2[i]:
#         print(1)
#         break
#     else:
#         print(-1)
#         break


# Pro Level Solution (Counter intuitive)

# a = input().lower()
# b = input().lower()
# print((a > b) - (a < b))