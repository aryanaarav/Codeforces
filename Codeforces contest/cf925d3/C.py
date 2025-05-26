import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()[:n]))
    l1=n
    r1=n
    
    for i in range(1,len(l)):
        if l[i] != l[i-1]:
            l1=i
            break
    for i in range(n-2,-1,-1):
        if l[i]!=l[i+1]:
            r1=n-i-1
            break
    
    ans=max(l1,r1)
    if l[0]==l[n-1]:
        ans=max(ans,l1+r1)
    print(max(n-ans,0))
    t -= 1