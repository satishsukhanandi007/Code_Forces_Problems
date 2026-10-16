n = int(input())
fibonacci_sequence = [0, 1]

for i in range(n):
    num = fibonacci_sequence[i] + fibonacci_sequence[i+1]
    fibonacci_sequence.append(num)
print(*fibonacci_sequence[0:n])