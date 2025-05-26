t = int(input())
count = 0
while t:
    s = input()
    if '+' in s:
        count += 1
    elif '-' in s:
        count -= 1
    t -= 1
print(count)
