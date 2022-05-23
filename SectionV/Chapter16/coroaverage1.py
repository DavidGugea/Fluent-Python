from coroutil import coroutine  # Import the coroutine decorator
from inspect import getgeneratorstate


@coroutine  # Apply it to the average function
def averager():  # The body of the function is exactly the same as in the previous example
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_avg = averager()  # Call averager(), creating

    print(getgeneratorstate(
        coro_avg))  # getgeneratorstate reports GEN_SUSPENDED, meaning that the coroutine is ready to receive a value

    print(coro_avg.send(10))  # You can immediately start sending values to coro_avg: that's the point of the decorator.
    print(coro_avg.send(30))
    print(coro_avg.send(5))
