k, s = map(int, input().split())
count = 0

# for x in range(k+1):  # for input 2900 3000 the time taken was 1027.24s
#     for y in range(k+1):
#         for z in range(k+1):
#             if x + y + z == s:
#                 count += 1
# print(count)


# Hard Coding using PnC: the time taken for the same input 2900 3000 was 0.02s

if s <= k:
    a = (s+2)
    s1 = a*(a-1)//2
    print(s1)
elif s <= 2*k:
    a, b = (s+2), (s-k+1)
    s1 = a*(a-1)//2
    s2 = b*(b-1)//2
    print(s1 - 3*s2)
elif s <= 3*k:
    a, b, c = (s+2), (s-k+1), (s-2*k)
    s1 = a*(a-1)//2
    s2 = b*(b-1)//2
    s3 = c*(c-1)//2
    print(s1 - 3*(s2-s3))
else:
    a, b, c, d = (s+2), (s-k+1), (s-2*k), (s-3*k-1)
    s1 = a*(a-1)//2
    s2 = b*(b-1)//2
    s3 = c*(c-1)//2
    s4 = d*(d-1)//2
    print(s1 - 3*(s2-s3) - s4)