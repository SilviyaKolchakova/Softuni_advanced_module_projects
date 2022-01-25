r, c = (int(x) for x in input().split())


matrix = []

for _ in range(r):
    matrix.append([x for x in input().split()])
square_2x2 = []
n= len(matrix)
m = len(matrix[0])
for row in range(n - 1):
    for c1 in range(m - 1):
        next_square = matrix[row][c1]\
        + matrix[row][c1+1]\
        + matrix[row+1][c1]\
        + matrix[row+1][c1+1]
        if matrix[row][c1]\
        == matrix[row][c1+1] == matrix[row+1][c1]\
        == matrix[row+1][c1+1]:
            square_2x2.append(next_square)

print(len(square_2x2))