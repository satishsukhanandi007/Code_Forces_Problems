n = int(input())
i = n+1
while True:
    l = list(map(int, str(i)))
    for x in l:
        if l.count(x) > 1:
            break
    i += 1
