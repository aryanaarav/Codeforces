s = input()
l = 0
a = s.index('^')
r = len(s) - 1
leftsum  = 0
rightsum = 0
while l < a:
    if s[l] != '=':
        leftsum += int(s[l])*((a)-l)
    l += 1
while r > a:
    if s[r] != '=':
        rightsum += int(s[r])*(r-(a))
    r -= 1
if leftsum == rightsum:
    print('balance')
elif leftsum > rightsum:
    print('left')
elif leftsum < rightsum:
    print('right')