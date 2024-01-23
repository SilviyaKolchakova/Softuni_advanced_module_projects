rows, columns = (int(x) for x in input().split(', '))

matrix = []

for r in range(rows):
    next_row = [int(x) for x in input().split()]
    matrix.append(next_row)

sum_columns = [0] * columns
for c in range(columns):
    for r in range(rows):
        current_value = matrix[r][c]
        sum_columns[c] += current_value

[print(x) for x in sum_columns]

