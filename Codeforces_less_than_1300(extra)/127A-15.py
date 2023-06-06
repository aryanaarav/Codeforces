import math

n, k = map(int, input().split())
a, b = map(int, input().split())
z = 0
for i in range(n-1):
    x, y = map(int, input().split())
    distance = math.sqrt((x-a)**2 + (y-b)**2)
    z += distance
    a = x
    b = y
print((k*z)/50)