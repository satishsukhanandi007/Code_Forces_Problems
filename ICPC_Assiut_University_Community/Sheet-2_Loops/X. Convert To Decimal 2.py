n = int(input())
for i in range(n):
    # n_binary_reverse = ""
    n = int(input())
    q = n
    count = 0
    num = 0
    while True:
        r = q % 2
        if r == 1:
            num += 2 ** (count)
            count += 1
        # n_binary_reverse += str(r)
        if q == r:
            break
        q //= 2
        # if q == 0:
        #     break
    # print(n_binary_reverse[::-1])
    print(num)