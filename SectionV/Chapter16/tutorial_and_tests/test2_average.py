def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro = averager()
    print(next(coro))
    print(coro.send(50))
    print(coro.send(100))
