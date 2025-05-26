

n, a, b, c = map(int,input().split())
k = 0 
ans = 0
for i in range(n // a + 1):
    for j in range(min((n - i * a) // b, n // c) + 1):
        rem = n - i * a - j * b
        if rem % c == 0:
            k = rem // c
            ans = max(ans, i + j + k)
print(ans)
