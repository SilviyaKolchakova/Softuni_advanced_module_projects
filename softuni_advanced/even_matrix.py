rows = int(input())
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

even_matrix = []
for row in range(len(matrix)):
    next_row = matrix[row]
    even_matrix.append([c for c in next_row if c % 2 == 0])
print(even_matrix)

