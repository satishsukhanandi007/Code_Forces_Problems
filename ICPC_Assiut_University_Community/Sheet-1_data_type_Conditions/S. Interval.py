n = float(input())
if 0 <= n <= 25:
    print("Interval [0,25]")
elif 25 < n <= 50:
    print("Interval (25,50]")
elif 50 < n <= 75:
    print("Interval (50,75]")
elif 75 < n <= 100:
    print("Interval (75,100]")
else:
    print("Out of Intervals")