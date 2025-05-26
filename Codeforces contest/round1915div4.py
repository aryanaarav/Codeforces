"""t = int(input())
while t:
    l1 = list(map(int, input().split()[:3]))
    for i in range(1, len(l1)):
        if l1[i] == l1[i-1]:
            continue
        else:
            print(l1[i])
            break
    t -= 1"""
    
t = int(input())
while t:
    mat = [input() for y in range(3)]
    l1 = 198
    for i in range(3):
        flag = 0
        l2 = 0
        for j in range(3):
            l2 += ord(mat[i][j])
        if l2 == l1:
            continue
        else:
            print(chr(l1 - l2))
            break
    t -= 1
    
"""t = int(input())
while t:
    C = R = 3
    mat = [input() for y in range(3)]
    print(mat)"""