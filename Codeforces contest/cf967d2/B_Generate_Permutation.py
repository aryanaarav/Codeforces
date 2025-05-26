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
t = int(input())
while t:
    l = []
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        l.append(1)
        for i in range(2,n+1):
            if i % 2 == 0:
                l.append(i+1)
            else:
                l.append(i-1)
        print(*l)
        


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