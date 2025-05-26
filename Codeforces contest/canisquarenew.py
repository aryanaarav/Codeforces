import math
t = int(input())
while t:
    n = int(input())
    l1 = list(map(int, input().split()[:n]))
    summ = sum(l1)
    k = math.isqrt(summ)
    if k*k == summ:
        print("YES")
    else:
        print("NO")
    t -= 1