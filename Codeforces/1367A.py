import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    s = input()
    s1 = ""
    i = 1
    while i < len(s)-1:
      s1 += s[i]
      i+=2
    s1 = s[0] + s1
    s1 = s1 + s[-1]
    print(s1)
    t -= 1