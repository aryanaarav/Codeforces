import math
t = int(input())
while t:
    n = int(input())
    l1 = list(map(int, input().split()[:n]))
    summ = sum(l1)
    if summ == 1:
        print("YES")
    left = 1
    right = summ//2
    while left <= right:
        flag = 0
        mid = left + (right - left)//2
        if mid*mid < summ:
            left = mid + 1
        elif mid*mid > summ:
            right = mid - 1
        elif mid*mid == summ:
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
    t -= 1