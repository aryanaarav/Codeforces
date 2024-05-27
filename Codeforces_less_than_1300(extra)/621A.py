n = int(input())
l1 = list(map(int, input().split()[:n]))
codd = 0
lodd = []
maxsum = 0
for i in range(len(l1)):
    if l1[i] % 2 == 1:
        codd += 1
        lodd.append(l1[i])
if codd > 0 and codd % 2 == 0:
    maxsum = sum(l1)
elif codd > 0 and codd % 2 == 1:
    maxsum = sum(l1) - min(lodd)
elif codd == 0:
    maxsum = sum(l1)
print(maxsum)