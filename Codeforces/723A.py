import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


x1,x2,x3 = map(int, input().split())
b = int((x1+x2+x3)/3)
print(abs(b - x1) + abs(b - x2) + abs(b - x3))