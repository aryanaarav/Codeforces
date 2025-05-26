s1 = input()
s2 = input()
s1 = s1.upper()
s2 = s2.upper()
flag = 0
for i in range(len(s1)):
    if ord(s1[i]) == ord(s2[i]):
        flag = 1
        continue
    elif ord(s1[i]) > ord(s2[i]):
        print(1)
        flag= 0
        break
    elif ord(s1[i]) < ord(s2[i]):
        print(-1)
        flag = 0
        break
if flag:
    print(0)