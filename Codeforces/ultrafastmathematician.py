s1 = input()
s2 = input()
s = ""
for i in range(len(s1)):
    if s1[i] != s2[i]:
        s += "1"
    elif s1[i] == s2[i] and s1[i] == '0':
        s += "0"
    elif s1[i] == s2[i] and s1[i] == '1':
        s += "0"
print(s)