n = int(input())
x = 0
for i in range(n):
    code = input()
    if "++" in code:
        x = x + 1
    else:
        x = x - 1
print(x)