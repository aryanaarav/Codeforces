import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())
s1 = ""
for i in range(m):
    s1 += "#"
s2 = "#"
for i in range(m-1):
    s2 = "." + s2
s4 = "#"
for i in range(m-1):
    s4 = s4 + "."
for i in range(1, n+1):
    if i % 2 == 1:
        print(s1)
    elif i % 2 == 0:
        if i % 4 == 0:
            print(s4)
        else:
            print(s2)
