from functools import wraps
from inspect import getgeneratorstate


def auto_prime_coroutine(generator_function):
    @wraps(generator_function)
    def primed_coroutine(*args, **kwargs):
        coroutine = generator_function(*args, **kwargs)
        next(coroutine)
        return coroutine

    return primed_coroutine


@auto_prime_coroutine
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        new_value = yield average
        total += new_value
        count += 1
        average = total / count


if __name__ == '__main__':
    coroutine = averager()
    """
    Coroutine states:
    
    1. GEN_CREATED -- > Coroutine started, no values yielded yet -- > the stack frame for this coroutine hasn't been built yet < -- 
    2. GEN_RUNNING -- > The interpreter is currently being executed by the interpreter -- > The coroutine still has values to yield
    3. GEN_SUSPENDED -- > The coroutine is suspended at an yield expression
    4. GEN_CLOSED -- > The coroutine is closed
    """
    print(
        getgeneratorstate(coroutine)
    )

