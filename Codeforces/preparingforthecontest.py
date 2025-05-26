t = int(input())
while t:
    n, k = map(int, input().split())
    l1 = []
    for i in range(n-k,n+1):
        l1.append(i)
    for j in range(n-k-1, 0,-1):
        l1.append(j)
    print(*l1)
    
    t -= 1