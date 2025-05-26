t = int(input())
l = list(map(int, input().split()[:t]))
print("EASY" if sum(l) == 0 else "HARD")