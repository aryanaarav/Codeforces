import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    for i in range(4):
        x, y = map(int, input().split())
        print(x,y)
    t-=1