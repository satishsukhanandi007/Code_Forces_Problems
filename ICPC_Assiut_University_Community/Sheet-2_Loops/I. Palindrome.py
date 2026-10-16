N = str(int(input()))
n = int(N[::-1])
# print(N,n)
if n == int(N):
    print(n, "YES", sep = "\n")
else:
    print(n, "NO", sep = "\n")