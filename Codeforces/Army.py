n = int(input())
l1 = list(map(int, input().split()[:n-1]))
a, b = map(int, input().split())
sum = 0
for i in range(a-1,b-1):
    sum += l1[i]
print(sum)