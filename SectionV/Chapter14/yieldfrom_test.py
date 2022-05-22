def chain(*iterables):
    for iterable in iterables:
        yield from iterable


def chain2(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


s = "ABC"
t = {1, 2, 3}

if __name__ == '__main__':
    print(list(chain(s, t)))
    print(list(chain2(s, t)))
