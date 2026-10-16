n = int(input())
numbers = list(map(int, input().split()))
even = 0
positive = 0
negative = 0
for i in range(n):
    if  numbers[i] % 2 == 0:
        even += 1
    if numbers[i] > 0:
        positive += 1
    elif numbers[i] < 0:
        negative += 1
print(f'''Even: {even})
Odd: {n-even}
Positive: {positive}
Negative: {negative}''')
    
    