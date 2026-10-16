cost, sell = map(int, input().split())
if cost < sell:
    print("Profit", sell - cost)
else:
    print("Loss", cost - sell)