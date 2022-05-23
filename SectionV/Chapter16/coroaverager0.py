def averager():
    total = 0.0
    count = 0
    average = None
    while True:  # This infinite loop means this coroutine will keep on accepting values and producing results as
        # long as the caller sends them. This coroutine will only terminate when the caller calls .close() on it,
        # or when it's garbage collected because there are no more references to it.
        term = yield average  # The yield statement here is used to suspend the coroutine, produce a result to the
        # caller, and -later- to get a value sent by the caller to the coroutine, which resumes the infinite loop.
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_avg = averager()  # Create the coroutine object

    print(next(coro_avg))  # Prime it by calling next

    print(coro_avg.send(10))  # Now we are in business: each call to .send() yields the current average
    print(coro_avg.send(30))
    print(coro_avg.send(5))
