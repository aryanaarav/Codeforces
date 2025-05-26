#                       oo0oo
#                     o8888888o
#                     88     88
#                     (| -_- |)
#                     0\  =  /0
#                    __/`---'\__
#                  .' \|     |// '.
#                 / \|||  :  |||// \|
#                / _||||| -:- |||||- \|
#               |   | \  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               |   | \  -  /// |  |
#               | \|  ''\---/''  |/ |
#               \  .-\__  '-'  ___/-. /
#             __'. .'  /--.--\  `. .'__
#          .        '<  `.\<|>/.' >'
#         | | :  - \.;\ _ /;.\`/ - ` : | |
#         \  \ _.   \_ __\ /__ _/   .- /  /
#            =====-.____.___ \/.-`_.-'=====
#                       `=---='    
# ========================================================
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  matrix = []
  for ii in range(n):
      row = list(map(int, input().split()))
      matrix.append(row)
  dy = [-1,0,1,0]
  dx = [0,-1,0,1]
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      mx=0
      for k in range(4):
        if 0 <= i + dx[k] < n and 0 <= j + dy[k] < m:
          mx = max(mx, matrix[i+dx[k]][j+dy[k]])
      if mx<matrix[i][j] and mx!=0:
        matrix[i][j] = mx
  for row in matrix:
      for element in row:
          print(element, end=" ")
      print()
      
      