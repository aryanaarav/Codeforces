import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
l = list(map(int, input().split()[:n]))
maxm = max(l)
minm = min(l)
maxi = l.index(maxm)
mini = 0
for i in range(n):
    if l[i] == minm:
        mini = i
if maxi > mini:
    print(maxi+n-1-mini-1)
else:
    print(maxi+n-1-mini)