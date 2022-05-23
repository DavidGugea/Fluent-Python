import functools


def coroutine(func):
    """Decorator: primes 'func' by advancing to first 'yield'"""

    @functools.wraps(func)
    def primer(*args, **kwargs):  # The decorated generator function is replaced by this primer function which,
        # when invoked, returns the primed generator
        gen = func(*args, **kwargs)  # Call the decorated function to get a generator object
        next(gen)  # Prime the generator
        return gen  # Return it

    return primer
