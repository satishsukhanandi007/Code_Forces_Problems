# n = int(input())
# store_new_abbreviation = []
# for i in range(n):
#     Long_word = input()
#     letters = list(Long_word) # Ex. ['S', 'h', 'y', 'a', 'm', ' ', 'S', 'u', 'k', 'h', 'a', 'n', 'a', 'n', 'd', 'i']
#     no_of_letters = len(letters) # 16
#     new_abbreviation = letters[0] + str(no_of_letters - 2) + letters[len(letters) - 1] # Ex. S14i
#     if (no_of_letters > 10):
#         store_new_abbreviation.append(new_abbreviation)
#     else:
#         store_new_abbreviation.append(Long_word)
# for i in store_new_abbreviation:
#     print(i)

n = int(input())
store_words = []
for names in range(n):
    word = input()
    if len(word) <= 10:
        store_words.append(word)
    else:
        abbreviation = word[0] + str(len(word)-2) + word[n-1]
        store_words.append(abbreviation)
for i in store_words:
    print(i)