import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


t = int(input())
while t:
    n, a, b = map(int, input().split())
    l = list(input())
    if a >= b:
        l1 = []
        count = 1
        for i in range(1,len(l)):
            if l[i] == l[i-1] and l[i] == 0:
                count +=1 
            else:
                l1.append(count)
                count = 0
        
        print(len(l)*a + len(set(l1))*b)
    else:
        print((len(l))*(a + b)) 
    
    t-=1