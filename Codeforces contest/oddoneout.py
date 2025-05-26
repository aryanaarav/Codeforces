t = int(input())
while t:
    l1 = list(map(int, input().split()[:3]))
    if l1[0] == l1[1]:
        print(l1[2])
    elif l1[1] == l1[2]:
        print(l1[0])
    elif l1[0] == l1[2]:
        print(l1[1])
    t -= 1