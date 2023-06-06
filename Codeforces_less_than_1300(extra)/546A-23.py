k, n, w = map(int, input().split())
base = k*((w**2+w)/2)
if n > base:
    print(0)
elif base >= n:
    print(int(base-n))