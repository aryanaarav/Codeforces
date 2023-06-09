n = int(input())
str1 = input()
count_of_X = 0
count_of_x = 0
for i in range(len(str1)):
    if str1[i] == "X":
        count_of_X += 1
    elif str1[i] == "x":
        count_of_x += 1
a = abs(count_of_X - count_of_x)//2
print(abs(count_of_X - count_of_x)//2)
if count_of_X > count_of_x:
    for j in range(a):
        str1_list = list(str1)
        for k in range(len(str1_list)):
            if str1_list[k] == "X":
                str1_list[k] = "x"
                break
        str1 = "".join(str1_list)
    print(str1)
elif count_of_x > count_of_X:
    for j in range(a):
        str1_list = list(str1)
        for k in range(len(str1_list)):
            if str1_list[k] == "x":
                str1_list[k] = "X"
                break
        str1 = "".join(str1_list)
    print(str1)
else:
    print(str1)