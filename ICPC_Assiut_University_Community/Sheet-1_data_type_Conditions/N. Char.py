X = input()
if 65  <= ord(X) <= 90:
    print(chr(ord(X) + 32))
else:
    print(chr(ord(X) - 32))