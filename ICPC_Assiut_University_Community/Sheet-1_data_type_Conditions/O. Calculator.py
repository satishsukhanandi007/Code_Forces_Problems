# print(int(eval(input())))


# String = input()
# if "+" in String:
# # if String.find("+") != -1:
#     a = String.find("+")
#     print(int(String[0:a]) + int(String[a+1:]))
# elif "-" in String:
# # elif String.find("-") != -1:
#     s = String.find("-")
#     print(int(String[0:s]) - int(String[s+1:]))
# elif "*" in String:
# # elif String.find("*") != -1:
#     m = String.find("*")
#     print(int(String[0:m]) * int(String[m+1:]))
# elif "/" in String:
# # elif String.find("/") != -1:
# # else:
#     d = String.find("/")
    # print(int(int(String[0:d]) / int(String[d+1:])))

S = input()

# for i, c in enumerate(S):
#     if c in "+-*/":
#         break
# print(i, c)

# for i in range(len(S)):
#     if S[i] in "+-*/":
#         c = S[i]
#         break

for c in "+-*/":
    if c in S:
        break
i = S.find(c)

A = int(S[:i])
B = int(S[i+1:])
if c == "+":
    print(A + B)
elif c == "-":
    print(A - B)
elif c == "*":
    print(A * B)
elif c == "/":
    print(int(A / B))
