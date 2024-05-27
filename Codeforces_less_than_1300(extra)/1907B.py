t = int(input())
while t > 0:
    s = input()
    k = ""
    for i in s:
        if ord(i) != 66 and ord(i) != 98:
            k += i
        elif ord(i) == 66:
            for j in range(len(k)-1, -1, -1):
                if ord(k[j]) >= 65 and ord(k[j]) <= 90:
                    k = k.replace(k[j], "")
                    break
        elif ord(i) == 98:
            for j in range(len(k)-1, -1, -1):
                if ord(k[j]) >= 97 and ord(k[j]) <= 122:
                    k = k.replace(k[j], "")
                    break    
        else:
            continue            
    print(k)
    t -= 1