message = ['h','e','l','l','o']
j = 0
s = input()
flag = 0
for i in s:
    if i == message[j]:
        j += 1
    if j == 5:
        flag = 1
        break
print("YES" if flag == 1 else "NO")
