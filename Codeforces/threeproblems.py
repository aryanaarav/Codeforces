n = int(input())
l1 = list(map(int, input().split()[:n]))
a = 1
b = 1
c = max(l1)
for j in range(len(l1)):
    if l1[j] != c:
        b = max(b, l1[j])
for j in range(len(l1)):
    if l1[j] != c and l1[j] != b:
        a = max(a, l1[j])
result = ((l1.index(a) + 1, l1.index(b) + 1, l1.index(c) + 1) if (a < b < c) and (a,b,c in l1) else (-1, -1, -1))
print(" ".join(map(str, result)))