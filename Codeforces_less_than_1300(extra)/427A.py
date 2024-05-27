n = int(input())
l1 = list(map(int, input().split()[:n]))
sum = 0
count = 0
for i in range(len(l1)):
    if l1[i] < 0:
        if sum == 0:
            count += 1
        else:
            sum -= 1
    else:
        sum += l1[i]
print(count)