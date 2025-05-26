import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())
while t:
    rating = int(input())
    if 1900 <= rating:
        print("Division 1")
    elif 1600 <= rating and rating <= 1899:
        print("Division 2")
    elif 1400 <= rating and rating <= 1599:
        print("Division 3")
    elif rating <= 1399:
        print("Division 4")
    t-=1