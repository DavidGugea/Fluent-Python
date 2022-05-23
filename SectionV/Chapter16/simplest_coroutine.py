def simple_coroutine():  # A coroutine is defined as a generator function: with yield in its body
    print('-> coroutine started')
    x = yield  # yield is used as an expression; when the coroutine is desgiend just to receive data from the client it yields None - this is implicit because there is no expression to the right of the yield keyword

    print('-> coroutine received: {0}'.format(x))


if __name__ == '__main__':
    my_coro = simple_coroutine()
    print(my_coro)  # As usual with generators, you call the function to get a generator object back
    print(
        next(my_coro)
        # The first call is next(...) because the generator hasn't started so it's not waiting in a yield and we can't send it any data initially.
    )
    print(
        my_coro.send(42)
        # This call makes the yield in the coroutine body evaluate to 42; now the courinted resumes and runs until the next yield or termination
    )

    # In this case, control flolws off the end of the coroutine body, which prompts the generator machinery to raise StopIteration, as usual