n = int(input())
str_clr = input()
str_clr_temp = str_clr + "$"
remove_num = 0

while str_clr_temp != "$":
        a = str_clr_temp[0]
        og_length = len(str_clr_temp) - 1
        if a == "R":
            b, c = str_clr_temp.find("G"), str_clr_temp.find("B")
            if b+1 and c+1:
                if b < c:
                    remove_num += b-1
                else:
                    remove_num += c-1
            elif b+1:
                remove_num += b-1
            elif c+1:
                remove_num += c-1
            elif og_length > 1:
                remove_num += og_length - 1
            str_clr_temp = str_clr_temp.lstrip("R")

        elif a == "G":
            b, c = str_clr_temp.find("R"), str_clr_temp.find("B")
            if b+1 and c+1:
                if b < c:
                    remove_num += b-1
                else:
                    remove_num += c-1
            elif b+1:
                remove_num += b-1
            elif c+1:
                remove_num += c-1
            elif og_length > 1:
                remove_num += og_length - 1
            str_clr_temp = str_clr_temp.lstrip("G")

        elif a == "B":
            b, c = str_clr_temp.find("R"), str_clr_temp.find("G")
            if b+1 and c+1:
                if b < c:
                    remove_num += b-1
                else:
                    remove_num += c-1
            elif b+1:
                remove_num += b-1
            elif c+1:
                remove_num += c-1
            elif og_length > 1:
                remove_num += og_length - 1
            str_clr_temp = str_clr_temp.lstrip("B")

print(remove_num)




# # length = n
# # remove_num = 0
# colour_string = input()
# count_R = colour_string.count("RR")
# count_G = colour_string.count("GG")
# count_B = colour_string.count("BB")

# if count_R > 0:
#     if 2 * count_R == n:
#         # length -= 2 * count_R - 1
#         remove_num += 2 * count_R - 1
#     elif 2 * count_R + 1 == n:
#         # length -= 2 * count_R
#         remove_num += 2 * count_R
#     else:
#         # length -= 2 * count_R
#         remove_num += 2 * count_R

# if count_G > 0:
#     if 2 * count_G == n:
#         # length -= 2 * count_G - 1
#         remove_num += 2 * count_G - 1
#     elif 2 * count_G + 1 == n:
#         # length -= 2 * count_G
#         remove_num += 2 * count_G
#     else:
#         # length -= 2 * count_G
#         remove_num += 2 * count_G

# if count_B > 0:
#     if 2 * count_B == n:
#         # length -= 2 * count_B - 1
#         remove_num += 2 * count_B - 1
#     elif 2 * count_B + 1 == n:
#         # length -= 2 * count_B
#         remove_num += 2 * count_B
#     else:
#         # length -= 2 * count_B
#         remove_num += 2 * count_B
 

# # print(n-length)
# print(remove_num)