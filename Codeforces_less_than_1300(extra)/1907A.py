t = int(input())
while t > 0:
    s = input()
    index = ord(s[0])
    for i in range(97,105):
        if i == index:
            continue
        else:
            print(chr(i) + str(s[1]))
    for i in range(1,9):
        if i == int(s[1]):
            continue
        else:
            print(chr(index) + str(i))
    t -= 1
