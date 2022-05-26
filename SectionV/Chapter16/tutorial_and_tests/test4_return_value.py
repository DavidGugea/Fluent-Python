from inspect import getgeneratorstate
from test3_coroutine_priming_decorator import auto_prime_coroutine
from collections import namedtuple

Result = namedtuple("Result", "count average")


@auto_prime_coroutine
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        new_value = yield average

        if new_value is None:
            break

        total += new_value
        count += 1
        average = total / count

    return Result(count, average)


if __name__ == '__main__':
    coroutine = averager()
    """
    Coroutine states:

    1. GEN_CREATED -- > Coroutine started, no values yielded yet -- > The only values on the stack frame saved for this coroutine are the arguments given to it, nothing else < --  
    2. GEN_RUNNING -- > The interpreter is currently being executed by the interpreter -- > The coroutine still has values to yield
    3. GEN_SUSPENDED -- > The coroutine is suspended at an yield expression
    4. GEN_CLOSED -- > The coroutine is closed
    """
    print(
        getgeneratorstate(coroutine)
    )

    print(coroutine.send(50))
    print(coroutine.send(100))

    try:
        print(coroutine.send(None))
    except StopIteration as e:
        print(e.value)