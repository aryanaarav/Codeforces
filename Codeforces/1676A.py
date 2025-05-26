import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


t = int(input())
while t:
    s = input()
    sl = s[:3]
    sr = s[3:]
    suml = 0
    sumr = 0
    for i in sl:
        suml += int(i)
    for i in sr:
        sumr += int(i)
    if suml == sumr:
        print("Yes")
    else:
        print("No")
    t-=1