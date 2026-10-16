n, a, b = map(int, input().split())
numbers = []

for number in range(1,n+1):
    sum_of_digits = 0
    # for digit in range(len(str(number))):
    #     sum_of_digits += int(str(number)[digit])
    for digit in str(number):
        sum_of_digits += int(digit)
    if a <= sum_of_digits <= b:
        numbers.append(number)
        # print(number, end = " ")
print(sum(numbers))