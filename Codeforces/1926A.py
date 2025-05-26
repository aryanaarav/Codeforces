import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    l = list(input())
    print(max(set(l), key = l.count))
    t-=1
    