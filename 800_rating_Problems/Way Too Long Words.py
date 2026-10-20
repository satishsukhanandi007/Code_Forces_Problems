# Third Attempt
n = int(input())
for _ in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        # print(word[0] + str(len(word)-2) + word[len(word)-1])
        print(F"{word[0]}{len(word)-2}{word[-1]}")


# Second Attempt
# n = int(input())
# store_words = []
# for _ in range(n):
#     word = input()
#     if len(word) <= 10:
#         store_words.append(word)
#     else:
#         abbreviation = word[0] + str(len(word)-2) + word[len(word)-1]
#         store_words.append(abbreviation)
# for name in store_words:
#     print(name)


# First Attempt
# # n = int(input())
# store_new_abbreviation = []
# for _ in range(n):
#     Long_word = input()
#     letters = list(Long_word)
#     no_of_letters = len(letters)
#     new_abbreviation = letters[0] + str(no_of_letters - 2) + letters[len(letters) - 1]
#     if (no_of_letters > 10):
#         store_new_abbreviation.append(new_abbreviation)
#     else:
#         # print(new_abbreviation)
#         store_new_abbreviation.append(Long_word)
# for name in store_new_abbreviation:
#     print(name)