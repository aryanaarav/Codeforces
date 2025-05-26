import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

from collections import Counter
t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()[:n]))
    a = Counter(l)
    count = 0
    for keys in a:
        if a[keys] >= 3:
            count += a[keys] // 3
    print(count)
    
    t-=1
    