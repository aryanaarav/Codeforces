n, k = map(int, input().split())
s = str(n)
print(s)
for i in range(k):
    r = n%10
    if r != 0:
        n -= 1
    elif r == 0:
        n = n//10
print(n)