import inspect


def func():
    print("Started the generator function")
    x = yield
    print("Ended the generator function")
    print('x -- > {0}'.format(x))


gen = func()

print(inspect.getgeneratorstate(
    gen  # GEN_CREATED - Waiting to start execution
))

next(gen)

print(inspect.getgeneratorstate(
    gen  # GEN_SUSPENDED - Currently suspended at a yield expression
))

try:
    next(gen)
except StopIteration as e:
    print(e)

print(inspect.getgeneratorstate(
    gen  # GET_CLOSED - Execution has completed
))
