s = input()
uppercase_letters = 0

for i in s:
    for j in range(65,91):
        if i == chr(j):
            uppercase_letters += 1

if uppercase_letters > len(s) // 2:
# if 2 * uppercase_letters > len(s):
# if uppercase_letters > len(s) - uppercase_letters:
    print(s.upper())
else:
    print(s.lower())