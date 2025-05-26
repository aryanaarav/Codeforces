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
    s = input()
    k = ""
    for i in s:
        if i == "p":
            k += "q"
        elif i == "q":
            k += "p"
        else:
            k += "w"
    print(k[::-1])


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