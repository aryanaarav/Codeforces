s = input()
s = list(s)
count1 = 0
count2 = 0
max1 = 0
max2 = 0
for i in s:
    if i == '1':
        count1 += 1
        max1 = max(max1, count1)
    elif i == '0':
        count1 = 0
for i in s:
    if i == '0':
        count2 += 1
        max2 = max(max2, count2)
    elif i == '1':
        count2 = 0
print("YES" if max1 >= 7 or max2 >= 7 else "NO")