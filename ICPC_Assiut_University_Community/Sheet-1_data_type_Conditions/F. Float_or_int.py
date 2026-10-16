n = input()
location = n.find(".")
# if location != -1:
if "." in n:
    integer_part = n[:location]
    fractional_part = n[location+1:]
    if int(fractional_part) == 0:
        print("int", int(float(n)))
    else:
        # print("float", int(float(n)), float(fractional_part)/(10 ** len(fractional_part)))
        print(f"float {int(float(n))} 0.{fractional_part}")
else:
    print("int", n)
