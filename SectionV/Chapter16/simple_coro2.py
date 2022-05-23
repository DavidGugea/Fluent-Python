from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> Started: a = {0}'.format(a))
    b = yield a
    print('-> Received: b = {0}'.format(b))
    c = yield a + b
    print('-> Received: c = {0}'.format(c))


if __name__ == '__main__':
    my_coro2 = simple_coro2(14)
    print(
        getgeneratorstate(my_coro2)
        # inspect.getgeneratorstate reports GEN_CREATED  (i.e., the coroutine has not started )
    )

    next(my_coro2)  # Advance Coroutine to first yield, printing -> Started: a = 14 message then yielding value of a and suspending to wait for value to be assigend to b

    print(
        getgeneratorstate(my_coro2) # getgeneratorstate reports GEN_SUSPENDED (i.e., the coroutine is paused at a yield expression )
    )

    my_coro2.send(28) # Send number 28 to suspended coroutine; the yield expression evaluates to 28 and that number is bound to b. The -> Received: b = 28 message is displayed, the value of aa + b is yieldedd(42), and the coroutine is suspended waiting for the value to be assigned to c.

    try:
        my_coro2.send(99) # Send number 99 to suspended coroutine; the yield expression evaluates to 99 the number is bound to c. The -> Received: c = 99 message is displayed, then the coroutine terminates, causing the generator ojbect to raise StopIteration.
    except StopIteration:
        pass

    print(getgeneratorstate(my_coro2)) # getgeneratorstate reports GEN_CLOSED (i.e., the coroutine execution has completed)