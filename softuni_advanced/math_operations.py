from collections import deque


def math_operations(*numbers, **operations_dict):
    numbers_que = deque(numbers)
    while numbers_que:
        operations_dict['a'] += numbers_que.popleft()
        if numbers_que:
            operations_dict['s'] -= numbers_que.popleft()
        if numbers_que:
            next_number = numbers_que.popleft()
            if next_number != 0:
                operations_dict['d'] /= next_number
        if numbers_que:
            operations_dict['m'] *= numbers_que.popleft()
    return operations_dict


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))