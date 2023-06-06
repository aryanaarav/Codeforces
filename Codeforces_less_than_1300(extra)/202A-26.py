str1 = input()
l1 = list(str1)
str_max = max(l1)
str2 = ""
for i in l1:
    if i == str_max:
        str2 += i
print(str2)