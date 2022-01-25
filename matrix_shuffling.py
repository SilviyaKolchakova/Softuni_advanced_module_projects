r, c = (int(x) for x in input().split())

matrix = []

for _ in range(r):
    matrix.append([x for x in input().split()])

next_command = input()
while next_command != 'END':
    command = next_command.split()
    if command[0] != 'swap':
        print('Invalid input!')
        next_command = input()
        continue
    if len(command) > 5 or len(command) < 5:
        print('Invalid input!')
        next_command = input()
        continue
    index1 = int(command[1])
    index2 = int(command[2])
    index3 = int(command[3])
    index4 = int(command[4])
    if 0 > index1 > r - 1 or 0 < index2 > c -1 or 0 > index3 > r - 1 or 0 < index4 > c -1:
        print('Invalid input!')
        next_command = input()
        continue
    else:
        matrix[index1][index2], matrix[index3][index4] = matrix[index3][index4],matrix[index1][index2]
        for el in matrix:
            print(' '.join(str(x) for x in el))
    next_command = input()
