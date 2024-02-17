def type_check(input_type):
    def decorator(func):
        def wrapper(el):
            if isinstance(el, input_type):
                return func(el)
            else:
                return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

