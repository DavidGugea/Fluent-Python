if __name__ == '__main__':
    test_list = [(a, b) for a, b in zip(range(1, 11), range(11, 21))]
    print(test_list)

    d1 = dict(test_list)
    print("d1: {0}".format(d1.keys()))
    d2 = dict(sorted(test_list))
    print("d2: {0}".format(d2.keys()))
    d3 = dict(sorted(test_list, key=lambda x:x[1]))
    print("d3: {0}".format(d3.keys()))
    assert d1 == d2 and d2 == d3
