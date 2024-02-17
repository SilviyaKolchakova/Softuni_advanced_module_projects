from time import time


def exec_time(func):
    def wrapper(*args):
        start_time = time()
        result = func(*args)
        end_time = time()
        return end_time - start_time

    return wrapper


@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())


