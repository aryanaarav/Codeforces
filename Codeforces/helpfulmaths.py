s = input()
l1 = []
for i in s:
    if i == '+':
        continue
    elif i != '+':
        l1.append(int(i))
l1.sort()
s1  = ""
for i in range(len(l1)):
    if i < len(l1) - 1:
        s1 += str(l1[i])
        s1 += '+'
    elif i == len(l1) - 1:
        s1 += str(l1[i])
print(s1)
        