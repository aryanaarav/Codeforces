l1 = list(map(int, input().split()[:4]))
s = input()
sum = 0
for i in range(len(s)):
    sum += l1[int(s[i])-1]
print(sum)
