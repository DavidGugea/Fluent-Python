from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # Same average coroutine. Here it is the subgenerator
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # Each value sent by the client code in main will be bound to term here.
        if term is None:  # The crucial terminating condition. Without it, a yield from calling this coroutine will
            # block forever
            break
        total += term
        count += 1
        average = total / count

    return Result(count, average)  # The return Result will be the value of the yield from expression in grouper


# the delegating generator
def grouper(results, key):  # grouper is the delegating generator
    while True:  # Each iteration in this loop creates a new instance of averager; each is a generator object
        # operating as a coroutine
        results[key] = yield from averager()  # Whenever grouper is sent a value, it's piped into the averager
        # instance by the yield from. grouper will be suspended here as long as the averager instance is consuming
        # values sent by the client. When an averager instance runs to the end, the value it returns is bound to
        # results[key]. The while loop then proceeds to create another averager instance to consume more values.


# the client code, a.k.a. the caller
def main(data):  # main is the client code, or "caller" in PEP 380 parlance. This is the function that drives everything
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # group is a generator object resulting from calling grouper with the results
        # dict to collect the results, and a particular key. It will operate as a coroutine.
        next(group)  # Prime the coroutine

        for value in values:
            group.send(value)  # Send each value into the grouper. That value ends up in the term = yield line of
            # averager; grouper never has a chance to see it.
        group.send(None)  # important !  # Sending None into grouper causes the current averager instance to
        # terminate, and allows grouper to run again, which creates another averager for the next group of values

    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print("{0:2} {1:5} averaging {2:.2f}{3}".format(
            result.count,
            group,
            result.average,
            unit
        ))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
        [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)
