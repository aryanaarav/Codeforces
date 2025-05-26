from collections import Counter
s1 = input()
s2 = input()
s3 = input()
s = s1+s2
s = sorted(s)
s3 = sorted(s3)
print("YES" if s == s3 else "NO")