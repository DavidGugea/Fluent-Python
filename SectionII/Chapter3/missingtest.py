class TestDict(dict):
    def __missing__(self, key):
        print("Missing key -- > {0}".format(key))


if __name__ == '__main__':
    t = TestDict()
    t['a'] = 1
    t['b'] = 2
    t['c'] = 3

    print(t)
    print(t['d'])
