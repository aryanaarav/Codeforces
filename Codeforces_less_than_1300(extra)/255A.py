n = int(input())
l1 = list(map(int, input().split()[:n]))
chest = 0
biceps = 0
back = 0
a = 0
b = 1
c = 2
for i in range(len(l1)):
    if a <= len(l1)-1:
        chest += l1[a]
    if b <= len(l1)-1:
        biceps += l1[b]
    if c <= len(l1)-1:
        back += l1[c]
    else:
        break
    a += 3
    b += 3
    c += 3
k  = max(chest, biceps, back)
if k == chest:
    print("chest")
elif k == biceps:
    print("biceps")
elif k == back:
    print("back")