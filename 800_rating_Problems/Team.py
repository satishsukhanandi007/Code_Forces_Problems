n = int(input())
solve = 0
for i in range(n):
    a,b,c = map(int, input().split())
    if(a+b+c>=2):
        solve = solve + 1
print(solve)