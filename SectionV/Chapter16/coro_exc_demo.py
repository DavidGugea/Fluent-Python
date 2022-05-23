class DemoException(Exception):
    """An exception type for the demonstration."""


def demo_exc_handling():
    print('-> coroutine started')

    while True:
        try:
            x = yield
        except DemoException:  # Special handling for DemoException
            print("*** DemoException handled. Cotinuin... ")
        else:
            print("-> coroutine received: {!r}".format(x))

    raise RuntimeError("This line should never run.")  # This line will never be executed


if __name__ == '__main__':
    exc_coro = demo_exc_handling()
    next(exc_coro)
    print(exc_coro.send(11))
    print(exc_coro.send(22))
    exc_coro.close()
    from inspect import getgeneratorstate
    print(getgeneratorstate(exc_coro))
