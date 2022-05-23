import inspect


def generator_builder():
    print("Started generator")
    x = yield 5
    y = yield 10
    print("Ended generator")

    print("x: {0}".format(x))
    print("y: {0}".format(y))


gen = generator_builder()

print(inspect.getgeneratorstate(gen))
print("-" * 50)
print(next(gen))
print("-" * 50)
print(inspect.getgeneratorstate(gen))
print("-" * 50)
print(next(gen))
print("-" * 50)
print(inspect.getgeneratorstate(gen))
print("-" * 50)
try:
    print(next(gen))
except StopIteration as e:
    print(e)
print("-" * 50)
print(inspect.getgeneratorstate(gen))
