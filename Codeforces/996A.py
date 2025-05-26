import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
a = 0
a += n//100
n = n%100
print("100 = ", a)
r = 20
while n % 5 < 5 and r >= 5:
    a += n // r
    b = n//r
    n = n%r
    print(r,"= ",b)
    if n < 5:
        break
    r = r//2
print("1 = ", n%5)
print("total = ",a+n%5)