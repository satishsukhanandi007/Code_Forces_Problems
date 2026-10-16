n,k = map(int, input().split())
scores = list(map(int, input().split()))
score_of_aK = scores[k-1]
cnt = 0
for i in scores:
    if i >= score_of_aK and i>0:
        cnt+=1
    else:
        break
print(cnt)