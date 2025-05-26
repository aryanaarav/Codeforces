import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split()[:n]))
    a = sorted(a)
    s = 0
    for i in range(1,len(a)):
        s += a[i]-a[i-1]
    print(s)
    t -= 1

