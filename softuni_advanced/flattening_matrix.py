rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = [n for sublist in matrix for n in sublist]

print(flattened_matrix)