t = int(input())
while t > 0:
    spaces = int(input())
    stringsymbol = input()
    count = 0
    for i in range(len(stringsymbol)):
        if i == ".":
            count += 1
            continue
        if count >= 3:
            break
        elif count < 3 and i == "#":
            count = 0
            print(stringsymbol.count("*"))
    print(stringsymbol.count('*'))
    
                