a, b, c, d = map(int, input().split())
ans = "NO"
for first_op in "+-*":
    for sec_op in "+-*":
        if first_op != sec_op:
            string = str(a) + first_op + str(b) + sec_op + str(c)
            if eval(string) == int(d):
                ans = "YES"
                # print(f"{string}={eval(string)}")
                break
print(ans)
