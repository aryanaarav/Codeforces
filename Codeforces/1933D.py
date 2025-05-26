import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()[:n]))
    num = l[0]
    print(num)
    for i in range(1,len(l)):
        num = num%l[i]
        print(num)
    print("YES" if num !=0 else "NO")
    t-=1