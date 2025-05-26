import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

"""
                        oo0oo
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    __/`---'\__
                  .' \|     |// '.
                 / \|||  :  |||// \|
                / _||||| -:- |||||- \|
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               |   | \  -  /// |  |
               | \|  ''\---/''  |/ |
               \  .-\__  '-'  ___/-. /
             __'. .'  /--.--\  `. .'__
          ."" '<  `.\<|>/.' >' "".
         | | :  - \.;\ _ /;.`/ - ` : | |
         \  \ _.   \_ __\ /__ _/   .- /  /
            =====-.____.___ \/.-`_.-'=====
                       `=---='    
========================================================"""
t = int(input())
while t:
    n = int(input())
    nums = list(map(int, input().split()[:n]))
    pre_max = 0
    total_sum = 0
    mx_diff = 0
    for num in nums:
      pre_max = max(pre_max, num)
      mx_diff = max(mx_diff, pre_max - num)
      total_sum += pre_max - num
    print(total_sum + mx_diff)
    t-=1 
