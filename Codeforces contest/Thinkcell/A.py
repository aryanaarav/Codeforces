import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()[:2*n]))
    count = 0
    for i in range(n):
        max1 = max(l)
        l.remove(max1)
        max2= max(l)
        l.remove(max2)
        count += min(max1, max2)
    print(count)
    t-= 1