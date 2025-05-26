n,  k =  map(int, input().split())
if k < 3*n:
    print(3*n - k)
elif 3*n<=k:
    print(0)