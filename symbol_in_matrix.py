n = int(input())

matrix = []
for r in range(n):
    next_row = input()
    matrix.append(next_row)

symbol = input()
symbol_found = False
row_number, column_number = None, None

for row in range(len(matrix)):
    if symbol in matrix[row]:
        row_number = row
        column_number = matrix[row].index(symbol)
        symbol_found = True
        break

if symbol_found:
    print(f'({row_number}, {column_number})')

else:
    print(f'{symbol} does not occur in the matrix')


