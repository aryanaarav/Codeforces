import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
t = int(input())
while t:
    n = int(input())
    s = input()
    nums = [int(x) for x in s.split(' ')]
    d = {}
    word = ""
    count = 97
    for num in nums:
        if num == 0:
            d[chr(count)] = 0
            count += 1
        else:
            for key, value in d.items():
                if value == num-1:
                    word += key
                    d[key] += 1
    print(word)
    t-=1
