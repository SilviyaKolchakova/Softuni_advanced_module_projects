rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    next_row = [int(x) for x in input().split(', ')]

    matrix.append(next_row)

n = len(matrix)
m = columns
sums = []
for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1]
        sums.append((current_sum, r, c))
max_sum = 0
target_square = None

for sum in range(len(sums)):
    current_sum = sums[sum][0]
    if current_sum > max_sum:
        max_sum = current_sum
        target_square = sums[sum]

index1 = target_square[1]
index2 = target_square[2]
print(f'{matrix[index1][index2]} {matrix[index1][index2 + 1]}')
print(f'{matrix[index1 + 1][index2]} {matrix[index1 + 1][index2 + 1]}')

print(f'{max_sum}')