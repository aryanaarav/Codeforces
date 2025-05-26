t = int(input())
while t:
    a, b = map(int, input().split())
    if a % 2 == 0 and b % 2 == 0:
        print(b*2)
    elif a == 1:
        print(b**2)
    elif (b%2 == 1 and a%2 == 1) or ((a+b) % 2 == 1):
        print(a*b)
    t-= 1