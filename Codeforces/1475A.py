import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    if n%2==1:
        print("YES")
    else:
        while n%2 == 0:
            n = n//2
        print("NO" if n%2 == 1 else "YES")
    t-=1