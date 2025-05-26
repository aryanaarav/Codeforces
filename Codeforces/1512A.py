import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

from collections import Counter
t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()[:n]))
    l1 = Counter(l)
    l2 = l1.values()
    for i in l1:
        if l1[i] == 1:
            print(l.index(i)+1)
    t-=1
