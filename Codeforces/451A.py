import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


n, m = map(int, input().split())
if n == 1 or m == 1:
    print("Akshat")
else:
    if min(n, m) % 2 == 1:
        print("Akshat")
    else:
        print("Malvika")
