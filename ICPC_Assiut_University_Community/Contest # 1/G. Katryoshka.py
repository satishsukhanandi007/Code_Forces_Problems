n, m, k = map(int, input().split())
if (n and k) > 0:
    if m > 0:
        if m < n and m < k:
            remaining_eyes = n-m
            remaining_bodies = k-m
            if remaining_eyes//2 > remaining_bodies :
                print(m + remaining_bodies)
            else:
                print(m + remaining_eyes//2)
        elif n < k:
            print(n)
        else:
            print(k)
else:
    print(0)