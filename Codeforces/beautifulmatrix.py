matrix = []
row = 0
col = 0
for i in range(5):
    s = list(input().split())
    matrix.append(s)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == '0':
            continue
        elif matrix[i][j] == '1':
            row = i
            col = j
print(abs(2-row)+abs(2-col))

