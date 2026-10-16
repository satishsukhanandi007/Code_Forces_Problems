n, k = map(int, input().split())
numbers = list(map(int, input().split()))
min_num_list = []

for i in range(0,n,k):
    min_num_list.append(min(numbers[i:i+k]))
print(*min_num_list)

# p = n//k*k
# for i in range(0,n,k):
#     temp_list = []
#     if i < p:
#         for j in range(k):
#             temp_list.append(numbers[i+j])
#         min_num_list.append(min(temp_list))
#     else:
#         for m in range(n%k):
#             temp_list.append(numbers[p + m])
#         min_num_list.append(min(temp_list))
# print(*min_num_list)
