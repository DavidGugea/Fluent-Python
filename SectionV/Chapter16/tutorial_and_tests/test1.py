import inspect


def simple_coroutine(a):
    print("-- > Started : a = {0}".format(a))
    b = yield a
    print("--> Received : b = {0}".format(b))
    c = yield a + b
    print("--> Received : c = {0}".format(c))


if __name__ == '__main__':
    coro = simple_coroutine(23)
    print(inspect.getgeneratorstate(coro))
    print(next(coro))
    print(coro.send(50))
    try:
        print(coro.send(150))
    except StopIteration as e:
        print(e)
