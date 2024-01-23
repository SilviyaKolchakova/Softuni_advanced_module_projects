rows, columns = (int(x) for x in input().split(', '))

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

the_sum = 0

for r in range(len(matrix)):
    ro = matrix[r]
    the_sum += sum(ro)

print(the_sum)


print(matrix)

