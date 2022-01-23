def fill_the_box(height, width,length, *command):
    box_area = height * width * length
    free_space_exceeded = False
    remaining_cubes = 0
    for el in command:
        if el == 'Finish':
            break
        if int(el) <= box_area:
            box_area -= int(el)
        else:
            free_space_exceeded = True
            remaining_cubes += int(el) - box_area
            box_area -= box_area
    if free_space_exceeded:
        return f'No more free space! You have {remaining_cubes} more cubes.'
    else:
        return f'There is free space in the box. You could put {box_area} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
