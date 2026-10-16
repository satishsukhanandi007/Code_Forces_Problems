# print(-10//3)
# print(-10%3)

# a = [10, 20, 30, 40,50,60]

# print(a[0])
# print(a[-1])
# print(a[0:5:1])

# l = list(map(int, input().split()))
# n = int(input())
# cnt = 0
# for i in range(len(l)):
#     if l[i] == n:
#         cnt += 1
# print(cnt)

# l = list(map(int, input().split()))
# n = l[0]
# for i in range(1, len(l)):
#     if l[i] > n:
#         n = l[i]
# print(n)

# a = input().split()
# print(a)

# print(int(-10.4))

# x = map(int, ["10", "20", "30"])
# print(x, list(x))

# x = "10 20".split()
# print(x)

# n = int(input())
# integers = list(map(int, input().split()))
# x = int(input())
# cnt = 0
# for i in integers:
#     if i == x:
#         cnt += 1
# print(cnt)

# n = int(input())
# integers = list(map(int, input().split()))
# x = 10
# cnt = 0
# for i in integers:
#     if i > x:
#         cnt += 1
# print(cnt)


# n = int(input())
# integers = list(map(int, input().split()))
# x = 2
# cnt = 0
# for i in integers:
#     if i % x == 0:
#         cnt += 1
# print(cnt)


# n = int(input())
# integers = list(map(int, input().split()))
# x = 2
# cnt = 0
# for i in integers:
#     if i % x == 0:
#         cnt += 1
# print(cnt, n - cnt, sep = "\n")


# n = int(input())
# integers = list(map(int, input().split()))
# x = 2
# cnt = 0
# for i in integers:
#     if i % x == 0:
#         cnt += 1
# print(cnt, n - cnt, sep = "\n")

# n = int(input())
# integers = list(map(int, input().split()))
# total = 0 # avoid using "sum" as a variable name because it is a built in function
# for i in integers:
#     total += i
# print(sum)

# print(sum([2,4,6,8]))


# n = int(input())
# integers = list(map(int, input().split()))
# even_total = 0 # avoid using "sum" as a variable name because it is a built in function
# odd_total = 0
# for i in integers:
#     if i % 2 == 0:
#         even_total += i
#     else:
#         odd_total += i
# print("Sum of Even numbers: ", even_total)
# print("Sum of Odd numbers: ", odd_total)


# n = int(input())
# integers = list(map(int, input().split()))
# cnt = 0
# # total = 0
# for i in integers:
#     if 10 <= i <= 20:
#         cnt += 1
#     # if i >= 10:
#     #     if i <= 20:
#     #         cnt += 1
#     # if i >= 10 and i <= 20:
#     #     cnt += 1
#         # total += i
# print(cnt)
# # print(total)


# n = int(input())
# integers = list(map(int, input().split()))
# x = int(input())
# # first_occurrence_of_x = str(x) + " is not present in the list"
# occurrences = []
# nth_occurrence_of_x_in_integers = 1
# for i in range(len(integers)):
#     # if integers[i] == x:
#     #     first_occurrence_of_x = i + 1
#     #     break
#     if integers[i] == x:
#         occurrences.append(i+1)
# print(occurrences[nth_occurrence_of_x_in_integers - 1])
# # print(first_occurrence_of_x)


# n = int(input())
# integers = list(map(int, input().split()))
# x = int(input())
# for i, value in enumerate(integers):
#     if value == x:
#         print(i+1)
#         break

