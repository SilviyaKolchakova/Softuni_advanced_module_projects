def concatenate(*elements):
    new_string = ''
    for el in elements:
        new_string += el

    return new_string


# print(concatenate("I", " ", "Love", " ", "Python"))