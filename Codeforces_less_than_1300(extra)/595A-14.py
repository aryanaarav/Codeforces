n, m = map(int, input().split())
count = 0
for i in range(n):
    a = list(map(int, input().split()[:2*m]))
    for j in range(2*m):
        if j % 2 == 0:
            if a[j] == 1 or a[j+1] == 1 or (a[j] == 1 and a[j+1] == 1):
                count += 1
print(count)