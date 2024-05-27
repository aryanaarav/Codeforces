s = input()
t = input()
count = 1
pointer_at_t = 0
pointer_at_s = 0
for i in range(len(t)):
    if t[pointer_at_t] == s[pointer_at_s]:
        count += 1
        pointer_at_t += 1
        pointer_at_s += 1
    else:
        pointer_at_t += 1
print(count)