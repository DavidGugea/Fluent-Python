def d1(func):
    print("Inside the decorator d1")

    return func


def d2(func):
    def inner(a, b):
        print("START -- d2 -- START")
        func(a, b)
        print("END -- d2 -- END")

    return inner


def test(a, b):
    print(a + b)


test = d2(test)


test(10, 11)
test(2, 3)
