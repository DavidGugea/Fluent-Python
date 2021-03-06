def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print([x.cell_contents for x in avg.__closure__])