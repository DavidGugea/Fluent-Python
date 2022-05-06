def deco(func):
    def inner():
        print("runnig inner()")

    return inner


@deco
def target():
    print("running target")


target()
print(target)
