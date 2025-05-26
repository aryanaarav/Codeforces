s = input()
up = 0
low = 0
for i in s:
    if i == i.upper():
        up += 1
    elif i == i.lower():
        low += 1
if up == low:
    print(s.lower())
elif up > low:
    print(s.upper())
elif up < low:
    print(s.lower())