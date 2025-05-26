import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())

while t:
    n = int(input())
    s = list(input())
    if len(s) == 1:
        print()
    
    t-=1
