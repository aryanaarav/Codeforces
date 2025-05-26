t = int(input())
while t:
    a = 1
    b = 1
    c = 1
    d = 1
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        if x > 0:
            a = 0
        if y > 0:
            b = 0
        if x < 0:
            c = 0
        if y < 0:
            d = 0
    if a+b+c+d == 0:
        print("NO")
    else:
        print("YES")
        
    
    t -= 1