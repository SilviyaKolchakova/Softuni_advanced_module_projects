def valid_coordinates(size, r, c):
    if r < 0 or c < 0 or r >= size or c >= size:
        return False
    return True


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

next_command = input()
while next_command != 'END':
    command = next_command.split()
    action = command[0]
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    if valid_coordinates(rows, row, col):
        if action == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value





    else:
        print("Invalid coordinates")
        next_command = input()
        continue
    next_command = input()

for r in matrix:
    print(*r)
