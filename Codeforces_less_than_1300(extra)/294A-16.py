n = int(input())
a = [int(i) for i in input().split()]
m = int(input())
for i in range(m):
    wire , bird = [int(j) for j in input().split()]
    if wire < n:
        a[wire] += a[wire - 1] - bird
 
    if wire - 2 >= 0:
        a[wire - 2] += bird - 1
 
    a[wire - 1] = 0
 
for j in range(n):
    print(a[j])