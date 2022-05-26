from inspect import getgeneratorstate


def countdown(n):
    print("Counting down from {0}".format(n))

    while n > 0:
        yield n
        n -= 1


if __name__ == '__main__':
    x = countdown(10)
    print(getgeneratorstate(x))
