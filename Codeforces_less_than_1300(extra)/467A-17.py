i = int(input())
count = 0
while i:
    p, q = map(int, input().split())
    if q-p >= 2:
        count += 1
    i -= 1
print(count)