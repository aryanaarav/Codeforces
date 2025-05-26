import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n=int(input())
    l=list(map(int,input().split(" ")))
    k=sum(l)
    d={1:0,2:0}
    if k%3==0:
        print(0)
    elif k%3==1:
        for i in l:
            if int(i%3)==1:
                d[1]+=1
            elif int(i%3)==2:
                d[2]+=1
        if d[1]>0:
            print(1)
        else:
            print(2)
        
    else:
        print(1)

    t-=1