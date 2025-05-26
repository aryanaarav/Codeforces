import math
n = int(input())
l = []
for i in range(2,20):
    count = 0
    print(i)
    for j in range(1,int(math.sqrt(i))+1):
        if i % j == 0:
            count += 1
    if count == 1:
        l.append(i)
        print(l)
print(l)