import functools

import time


def benchmark(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time of %s - %s s" % (func.__name__, end_time - start_time))
        return result

    return inner


@benchmark
def foo():
    return 'foo'


print(foo())
