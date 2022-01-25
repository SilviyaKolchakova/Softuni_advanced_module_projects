n = int(input())

matrix = [[int(x) for x in input().split()] for j in range(n)]

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    primary_diagonal.append((matrix[row][row]))
    secondary_diagonal.append((matrix[row][n - 1 - row]))

primary_diagonal_sum = (sum(primary_diagonal))
secondary_diagonal_sum = (sum(secondary_diagonal))

print(abs(primary_diagonal_sum - secondary_diagonal_sum))