str1 = input()
str2 = input()
str3 = input()
str1 = str1.strip()
str2 = str2.strip()
str3 = str3.strip()
c1 = 0
c2 = 0
c3 = 0
for i in str1:
    if i == 'a':
        c1 += 1
    elif i == 'e':
        c1 += 1
    elif i == 'i':
        c1 += 1
    elif i == 'o':
        c1 += 1
    elif i == 'u':
        c1 += 1
for j in str2:
    if j == 'a':
        c2 += 1
    elif j == 'e':
        c2 += 1
    elif j == 'i':
        c2 += 1
    elif j == 'o':
        c2 += 1
    elif j == 'u':
        c2 += 1
for k in str3:
    if k == 'a':
        c3 += 1
    elif k == 'e':
        c3 += 1
    elif k == 'i':
        c3 += 1
    elif k == 'o':
        c3 += 1
    elif k == 'u':
        c3 += 1
if c1 == 5 and c2 == 7 and c3 == 5:
    print("YES")
else:
    print("NO")