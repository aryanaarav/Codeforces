import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    n = int(input())
    l = list(input())
    if n == 1:
        print(0)
    else:
        c = 0
        for i in range(1, n):
            if l[i] == '.':
                continue
            elif l[i] == '@':
                c += 1
            elif l[i] == '*':
                if i != n-1:
                    if l[i+1] == '*': 
                        break
                if i == n-1:
                        break
                else:
                    continue
        print(c)
    
    t-=1