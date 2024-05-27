n = int(input())
l1 = []
l2 = []
while n:
    home, guest = map(int, input().split())
    l1.append(home)
    l2.append(guest)
    n -= 1
count = 0
for i in range(0,len(l1)):
    for j in range(0,len(l2)):
        if i != j:
            count += (l1[i] == l2[j])
print(count)

        