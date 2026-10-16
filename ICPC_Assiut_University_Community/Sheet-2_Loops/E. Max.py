n = int(input())
numbers = list(map(int, input().split()))
maxx = numbers[0]
for index in range(1, n):
    if numbers[index] > maxx:
        maxx = numbers[index]
print(maxx)
# print(max(mumbers))