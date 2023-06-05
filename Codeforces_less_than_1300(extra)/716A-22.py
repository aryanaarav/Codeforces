n, c = map(int, input().split())
l1 = list(map(int, input().split()[:n]))
l2 = []
count = -1
for i in range(1, len(l1)):
    if (l1[i]-l1[i-1]) <= c:
        l2.append(l1[i-1])
        l2.append(l1[i])
        count += 1
    elif (l1[i]-l1[i-1]) > c:
        l2 = []
        count = -1
print(len(l2)-count)