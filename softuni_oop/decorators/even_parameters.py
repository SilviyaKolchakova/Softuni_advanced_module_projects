def even_parameters(func):
    def wrapper(*args):
        # for el in args:
        #     try:
        #         if not el % 2 == 0:
        #             return "Please use only even numbers!"
        #     except:
        #         return "Please use only even numbers!"
        if all([x % 2 == 0 for x in args]):
            return func(*args)
        else:
            return f"Please use only even numbers!"



    return wrapper



@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

