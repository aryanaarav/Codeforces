
n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = l1 + l2
a = []
for i in range(len(l3)):
    if l3[i] > 0:
        a.append(l3[i])
s = set(a)
print(len(s))
if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")