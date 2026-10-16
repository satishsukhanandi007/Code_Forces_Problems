S = input()
N = int(input())
numbers = map(int, input().split())

for i in numbers:
    print(S*i)