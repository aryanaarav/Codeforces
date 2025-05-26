t = int(input())
while t:
    k = int(input())
    print(k - 10**(len(str(k))-1))
    t -= 1