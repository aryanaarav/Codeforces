n, k = map(int, input().split())
l1 = list(input().split())
maincount = 0
for i in (l1):
    count = 0
    for j in range(len(i)):
        if i[j] == '4' or i[j] == '7':
            count += 1
    if count <= k:
        maincount += 1
print(maincount)