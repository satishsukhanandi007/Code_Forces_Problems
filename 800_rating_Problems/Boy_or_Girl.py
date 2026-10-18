user_name = input()
diff_char = len(user_name)

for i in range(97,123): # Lesser loop count because it is given that the input string is in lower case
# for i in range(255):
    count_letter = user_name.count(chr(i))
    if count_letter > 1:
        diff_char -= count_letter - 1
# print(diff_char)
if diff_char % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")


# -----------------------------------------------------------------------------------------------------


# list_characters = list(user_name)
# characters = [list_characters[0]]

# for i in range(1, len(list_characters)):
#     chrc = list_characters[i]
#     if chrc not in characters:
#         characters.append(chrc)
# print(len(characters))
# if len(characters) % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")


# -----------------------------------------------------------------------------------------------------


# list_characters = list(user_name)
# characters = [list_characters[0]]
# cnt = 0
# different = 1
# for i in range(1,len(list_characters)):
#     cnt = 0
#     characters.append(list_characters[i])
#     # print(characters)
#     for j in range(i):
#         if list_characters[i] == characters[j]:
#             cnt += 1
#     if cnt == 0:
#         different += 1
# print(different)
# if different % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")