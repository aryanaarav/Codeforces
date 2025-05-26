import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
l = list(map(int, input().split()[:n]))
m = 1
count = 1
for i in range(len(l)):
    if i > 0:
        if l[i] >= l[i-1]:
            count += 1
            m = max(m, count)
        else:
            
            count = 1
print(m)