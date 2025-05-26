t = int(input())
cap = 0
maxm = 0
while t:
    a, b = map(int, input().split())
    cap = cap - a + b
    maxm = max(cap, maxm)
    t -= 1
print(maxm)