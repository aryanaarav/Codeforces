t = int(input())
while t:
    mat = [list(input()) for i in range(3)]
    l1 = 198
    for i in range(3):
        l2 = 0
        for j in range(3):
            l2 += ord(mat[i][j])
        if l2 != l1:
            print(chr(l1-l2+63))
    t -= 1