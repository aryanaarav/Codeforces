a, b, c = map(int, input().split())
print("Yes" if c == abs(a) + abs(b) or ((c > abs(a)+abs(b)) and (c-abs(a)-abs(b))%2 == 0) else "No")