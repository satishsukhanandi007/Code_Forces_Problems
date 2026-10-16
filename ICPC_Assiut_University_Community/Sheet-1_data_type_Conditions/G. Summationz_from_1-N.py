n = int(input())
# print(int(n * (n + 1) / 2))   # Python integers have unlimited precision 
# print(n * (n + 1) / 2)        # But Python float is normally IEEE-754 binary64, which has 53 bits of precision. It cannot represent every integer this large exactly.
print(n * (n + 1) // 2)
# summation = 0
# for i in range(n):        # Not efficient for long calculations
#     summation += i + 1
# print(summation)
# while n > 0:            # Even Slower than for loop because it is calculating "summation" and 'n' at each 'n'
#     summation += n
#     n -= 1
# print(summation)