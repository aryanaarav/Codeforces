#                        oo0oo
#                      o8888888o
#                      88  .  88
#                      (| -_- |)
#                      0\  =  /0
#                    __/`---'\__
#                  .' \|     |// '.
#                 / \|||  :  |||// \|
#                / _||||| -:- |||||- \|
#               |   | \  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               |   | \  -  /// |  |
#               | \|  ''\---/''  |/ |
#               \  .-\__  '-'  ___/-. /|
#             __'. .'  /--.--\  `. .'__|
#          .'.' '<  `.\<|>/.' >' '.' |
#         | | :  - \.;\ _ /;.\`/ - ` : | |
#         \  \ _.   \_ __\ /__ _/   .- /  /
#            =====-.____.___ \/.-`_.-'=====
#                       `=---='    
# ========================================================
# Pranam
import math
t = int(input())
while t:
    n, a, b = map(int, input().split())
    gcd_ab = math.gcd(a, b)

    arr = list(map(int, input().split()))
    arr = [x % gcd_ab for x in arr] 

    arr.sort()

    ans = arr[-1] - arr[0]  
    for i in range(n - 1):
        ans = min(ans, arr[i] + gcd_ab - arr[i + 1]) 

    print(ans)


# Extracting columns from a matrix
    def extract_columns(grid):
        rows = len(grid)
        cols = len(grid[0])
        column_arrays = []
        for c in range(cols):
            column_array = [grid[r][c] for r in range(rows)]
            column_arrays.append(column_array)
        return column_arrays
    def SieveOfEratosthenes(num):
        prime = [True for i in range(num+1)]
        p = 2
        while (p * p <= num):
            if (prime[p] == True):
                for i in range(p * p, num+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, num+1):
            if prime[p]:
                print(p)
    t -=1