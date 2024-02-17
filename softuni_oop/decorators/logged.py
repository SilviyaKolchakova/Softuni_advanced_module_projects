def logged(dec_func):
    def wrapper(*args):
        result = dec_func(*args)
        return f"you called {dec_func.__name__}{args}\nit returned {result}"
    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

