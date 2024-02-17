def tags(tag):
    def decorator(func):
        def wrapper(*args):
            res = func(*args)
            return f"<{tag}>{res}</{tag}>"
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

