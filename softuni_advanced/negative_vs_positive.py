def sum_numbers(numbers):
    positive_num = 0
    negative_num = 0
    for num in numbers:
        if num > 0:
            positive_num += num
        else:
            negative_num += num
    if abs(negative_num) > positive_num:
        return negative_num, positive_num, "The negatives are stronger than the positives"

    return negative_num, positive_num, "The positives are stronger than the negatives"


my_numbers = ([int(x) for x in input().split()])

print(sum_numbers(my_numbers))
