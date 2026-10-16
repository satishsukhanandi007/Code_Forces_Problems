T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    temp_list = []
    for j in range(min(x,y)+1,max(x,y)):
        if j % 2 == 1:
            temp_list.append(j)
    print(sum(temp_list))