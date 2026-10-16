N = int(input())

for i in range(N):
    n = input()[::-1]
    temp_list = []
    for j in n:
        temp_list.append(j)
        # print(j, end = " ")
    # print()
    print(*temp_list)