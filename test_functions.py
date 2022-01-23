from collections import deque

command = input().split(', ')

cube = deque(command)
h, l, w = int(cube.popleft()), int(cube.popleft()), int(cube.popleft())
limit = h * l * w
cubes_made = 0
while cube:
    next_element = cube.popleft()
    if next_element != 'Finish':
        if int(next_element) < limit:
            cubes_made += int(next_element)
            limit -= int(next_element)
        else:
            cubes_left = (int(next_element) - limit) + sum([int(x) for x in cube])
            limit -= limit
    else:
        break
if limit > 1:
    print(f'There is free space in the box. You could put {limit} more cubes.')
else:
    print(f'No more free space! You have {sum(cube)} more cubes.')

