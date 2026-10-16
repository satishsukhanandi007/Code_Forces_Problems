a, b = map(int, input().split())
m = 0
for number in range(a,b+1):
    number = str(number)
    n = 0
    # print(number)
    for i in number:
        # print(i)
        if i == "4" or i == "7":
            n += 1
        else:
            break
    # print(n, len(number))
    if n == len(number):
        m += 1
        print(number, end = " ")
# print(f'''
# {m}''')
if m == 0:
    print(-1)