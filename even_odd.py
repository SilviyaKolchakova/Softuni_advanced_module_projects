def even_odd(*numbers):
    odd_nums = []
    even_nums = []
    for el in numbers[0:len(numbers) - 1]:
        if el % 2 == 0:
            odd_nums.append(el)
        else:
            even_nums.append(el)
    if numbers[-1] == 'odd':
        return even_nums
    return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
print(even_odd(1, 2, 3, 4, 5, 6, "even"))