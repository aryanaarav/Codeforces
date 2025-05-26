import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

tc = int(input())
while tc:
    n = int(input())
    l = list(map(int, input().split()[:n]))
    s=sum(l)//n
    ex=0
    t=1
    for i in range(n):
        if l[i]>s:
            ex+=l[i]-s
        else:
            if s-l[i]<=ex:
                ex-=s-l[i]
                l[i]=s
            else:
                t=0
                break
    if t:
        print("YES")
    else:
        print("NO")
    tc -= 1