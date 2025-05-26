import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
d = {}
l = []
for i in range(n):
    s = input()
    l.append(s)
for i in l:
    if i not in d:
        d[i] = 1
    elif i in d:
        d[i] += 1
k = max(d.values())
for i in d:
    if d[i] == k:
        print(i)
    

        
    