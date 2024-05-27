x = [500, 1000, 1500, 2000, 2500]
m = list(map(int, input().split()[:5]))
w = list(map(int, input().split()[:5]))
s, us = map(int, input().split())
sum = 0
for i in range(5):
    k = max(0.3*x[i], (1-(m[i]/250.0))*x[i] - (w[i]*50.0))
    print(k)
    sum += k
    print(sum)
sum += (100*s - 50*us)
print(int(sum))
