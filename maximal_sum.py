rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
max_row_index = 0
max_col_index = 0
n= len(matrix)
m = len(matrix[0])
for row in range(n - 2):
    for c1 in range(m - 2):
        next_square_sum = matrix[row][c1] +\
        matrix[row][c1+1] +\
        matrix[row][c1+2] +\
        matrix[row+1][c1] +\
        matrix[row+1][c1+1] +\
        matrix[row + 1][c1 + 2] +\
        matrix[row + 2][c1] +\
        matrix[row + 2][c1 + 1] +\
        matrix[row + 2][c1 + 2]
        if next_square_sum > max_sum:
            max_sum, max_row_index, max_col_index = next_square_sum, row, c1

print(f'Sum = {max_sum}')
print(matrix[max_row_index][max_col_index], matrix[max_row_index][max_col_index + 1], matrix[max_row_index][max_col_index + 2])
print(matrix[max_row_index + 1][max_col_index], matrix[max_row_index + 1][max_col_index + 1], matrix[max_row_index + 1][max_col_index + 2])
print(matrix[max_row_index + 2][max_col_index], matrix[max_row_index + 2][max_col_index + 1], matrix[max_row_index + 2][max_col_index + 2])



