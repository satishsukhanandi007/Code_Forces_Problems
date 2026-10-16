while True:
    N, M = map(int, input().split())

    if N <= 0 or M <= 0:
        break

    no_of_numbers = abs(M - N) + 1

    # Using function

    def print_num(n,m):
        print(n, end = " ")
        if m == numbers:
            return n
        return n + print_num(n+1,m+1)

    k = print_num(min(M, N),1)
    print(f"sum ={k}")


    # # Using Loops

    # summ = ((M + N) * (abs(M - N) + 1) // 2)

    # for i in range(min(M,N),max(M,N)+1):
    #     print(i, end = " ")
    # # print("sum =", summ, sep = "")
    # print(f"sum ={summ}")