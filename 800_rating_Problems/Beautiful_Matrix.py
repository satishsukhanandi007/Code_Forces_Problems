a = []
i = 0
j = 0
for r in range(5):
     row = list(map(int, input().split()))
     a.append(row)
for k in range(5):
    for integer in a[k]:
        if integer == 1:
            i = k + 1
            final_row = a[k]
            for n in range(5):
                    m = final_row[n]
                    if m == 1:
                        j = n + 1
if i <= 3:
     if j <= 3:
          print(6-i-j)
     else:
          print(j-i)
else:
     if j <= 3:
          print(i-j)
     else:
          print(i+j-6)