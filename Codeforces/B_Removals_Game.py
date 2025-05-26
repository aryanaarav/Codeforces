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
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    if l1 == l2 or l1 == l1 == l2[::-1]:
        print("Bob")
    else:
        print("Alice")

# Extracting columns from a matrix
    def extract_columns(grid):
        rows = len(grid)
        cols = len(grid[0])
        column_arrays = []
        for c in range(cols):
            column_array = [grid[r][c] for r in range(rows)]
            column_arrays.append(column_array)
        return column_arrays
    t -=1