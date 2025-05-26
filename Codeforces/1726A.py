import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    print(abs(l[0]-l[-1]))
    t-=1