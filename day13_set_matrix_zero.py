# Day 13 - Set Matrix Zeroes

matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

rows = set()
cols = set()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            rows.add(i)
            cols.add(j)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i in rows or j in cols:
            matrix[i][j] = 0

print(matrix)
