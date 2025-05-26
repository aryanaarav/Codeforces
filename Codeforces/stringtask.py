s = input()
k = ""
vowels = ['a','e','i','o','u','y']
for i in s:
    if i.lower() not in vowels:
        k = "." + k
        k = i.lower() + k
    elif i == i.upper() and i.lower() not in vowels:
        k = i.lower()
        s.replace(i, k)
    elif i.lower() in vowels:
        s.replace(i, "")
print(k[::-1])