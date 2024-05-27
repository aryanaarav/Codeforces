n = int(input())
l1 = list(map(int, input().split()[:n]))
s, t  = map(int, input().split())
if s == t:
    print(0)
else:
    print(min(sum(l1[min(s, t) - 1 : max(s, t) - 1 :]), sum(l1) - sum(l1[min(s, t) - 1 : max(s, t) - 1 :])))
