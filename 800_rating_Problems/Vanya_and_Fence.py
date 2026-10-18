n, h = map(int, input().split())
heights = list(map(int, input().split()))
minimum_total_width = 0

for x in heights:
    if x > h:
        minimum_total_width += 2
    else:
        minimum_total_width += 1
print(minimum_total_width)