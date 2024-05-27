n = int(input())
c1 = 0
c2 = 0
c3 = 0
while n > 0:
    x, y, z = map(int, input().split())
    c1 += x
    c2 += y
    c3 += z
    n -= 1
if c1 == c2 == c3 == 0:
    print("YES")
else:
    print("NO")