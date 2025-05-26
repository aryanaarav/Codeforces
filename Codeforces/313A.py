import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
if n > 0:
    print(n)
else:
    n = abs(n-0)
    s = str(n)
    l = list(s)
    l1 = l.copy()
    l.pop(len(l)-1)
    l1.pop(len(l1)-2)
    if int(''.join(l1)) < int(''.join(l)):
        print(int("-"+''.join(l1)))
    else:
        print(int("-"+''.join(l)))
                      
