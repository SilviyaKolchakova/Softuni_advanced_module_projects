n = int(input())

matrix = []
for r in range(n):
    next_row = [int(x) for x in input().split()]
    matrix.append(next_row)

the_sum = 0
for i in range(n):
    the_sum += matrix[i][i]

print(the_sum)