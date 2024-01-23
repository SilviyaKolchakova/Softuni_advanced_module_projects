def odd_or_even_sum(command, numbers):
    positive_num = 0
    negative_num = 0
    for num in numbers:
        if num % 2 == 0:
            positive_num += num
        else:
            negative_num += num
    if command == 'Even':
        return positive_num * len(numbers)
    return negative_num * len(numbers)


command = input()
my_numbers = ([int(x) for x in input().split()])
print(odd_or_even_sum(command, my_numbers))