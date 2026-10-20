n, k = map(int, input().split())
scores = list(map(int, input().split()))
base_score = scores[k-1]

cnt = 0
for x in scores:
    if x >= base_score and x > 0:
        cnt += 1
    else:
        break
print(cnt)


# if base_score > 0:
#     if min(scores) != base_score:
#         for i in range(n):
#             if scores[i] < base_score:
#                 print(i)
#                 break
#     else:
#         print(len(scores))
# else:
#     print(len(scores) - scores.count(0))