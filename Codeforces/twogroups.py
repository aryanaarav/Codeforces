t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()[:n]))
    print(abs(sum(l)))
    t -= 1