alphabet = input()
ord = ord(alphabet)
if ord == 122:
    print("a")
else:
    print(chr(ord + 1))