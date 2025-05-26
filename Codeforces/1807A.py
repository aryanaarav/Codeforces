import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    a, b, c = map(int, input().split())
    if c == a+b:
        print("+")
    else:
        print("-")
    t-=1