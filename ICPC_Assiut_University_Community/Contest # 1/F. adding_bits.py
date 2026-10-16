a, b = map(int, input().split())

def base_conversion(num):
    q = num
    new_num = ""
    while q > 0:
        r = q % 2
        new_num += str(r)
        q //= 2
    return new_num

new_a = base_conversion(a)
new_b = base_conversion(b)
addition = ""

if len(new_a) > len(new_b):
    l = len(new_b)
    extra = new_a[l:]
elif len(new_a) < len(new_b):
    l = len(new_a)
    extra = new_b[l:]
else:
    l = len(new_a)
    extra = ""

for i in range(l):
    # if new_a[i] == "1" == new_b[i]:
    #     addition += "0"
    # else:
    #     addition += str(int(new_a[i]) + int(new_b[i]))

    sum_i = int(new_a[i]) + int(new_b[i])
    if sum_i == 2:
        addition += "0"
    else:
        addition += f"{sum_i}"
        # addition += str(sum_i)

addition += extra
add = int(addition[::-1],2)
print(add)
