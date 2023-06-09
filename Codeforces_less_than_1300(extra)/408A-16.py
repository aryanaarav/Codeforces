n = int(input())
l1 = list(map(int, input().split()[:n]))
l3 = []
for j in l1:
    l2 = list(map(int, input().split()[:j]))
    t = 5 * (sum(l2)) + 15 * j
    l3.append(t)
print(min(l3))