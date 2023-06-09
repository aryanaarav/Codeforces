n, s = map(int, input().split())
l1 = list(map(int, input().split()[:n]))
flag = 0
for i in l1:
    if sum(l1) - i > s:
        flag = 1
    elif sum(l1) - i <= s:
        print("YES")
        flag = 0
        break
if flag == 1:
    print("NO")