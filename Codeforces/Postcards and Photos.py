s = input()
s = list(s)
maincount = 0
if len(s) == 1:
    print(1)
else:
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 0
        if count == 5:
            maincount += 1
            count = 0
print(maincount+1)
