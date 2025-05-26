import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
l = list(map(int, input().split()[:n]))
m = max(l)
sum = 0
for i in range(n):
    sum += abs(l[i]-m)
print(sum)
