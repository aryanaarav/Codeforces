disk = int(input())
l1 = []
str1 = input()
str2 = input()
steps = 0
for i in range(disk):
    if abs(int(str1[i])-int(str2[i])) > abs(10 - (abs(int(str1[i])-int(str2[i])))):
        steps += abs(10 - (abs(int(str1[i])-int(str2[i]))))
    if abs(int(str1[i]) - int(str2[i])) < abs(10 - (abs(int(str1[i]) - int(str2[i])))):
        steps += abs(int(str1[i]) - int(str2[i]))
    if abs(int(str1[i]) - int(str2[i])) == abs(10 - (abs(int(str1[i]) - int(str2[i])))):
        steps += abs(int(str1[i]) - int(str2[i]))
print(steps)