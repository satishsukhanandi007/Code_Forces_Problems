N = int(input())
n = 0
for number in range(2,N+1):
    n = 0
    for dividend in range(2,number):
        if number % dividend != 0:
            n += 1
        else:
            break
    if n == number - 2:
        print(number, end = " ")