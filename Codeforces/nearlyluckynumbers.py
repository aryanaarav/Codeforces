n = int(input())
l = list(str(n))
count = 0
for i in l:
    if i == '4' or i == '7':
        count += 1
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")