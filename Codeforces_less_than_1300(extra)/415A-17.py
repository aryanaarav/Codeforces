n, m = map(int, input().split())
l1 = list(map(int, input().split()[:m]))
l2 = []
for j in l1:
    for i in range(n, j-1, -1):
        if j <= i:
            l2.append(j)
        n = j-1
for k in range(len(l2)-1, -1, -1):
    print(str(l2[k]), end=" ")