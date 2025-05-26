t = int(input())
while t:
    a, b = map(int, input().split())
    print("Bob" if (a+b)% 2 == 0 else "Alice")
    t-= 1
