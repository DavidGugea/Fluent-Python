def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print(
        list(map(factorial, range(6)))
    )
    print(
        [factorial(n) for n in range(6)]
    )
    print(
        list(map(factorial, filter(lambda n: n % 2, range(6))))
    )
    print(
        [factorial(n) for n in range(6) if n % 2 == 0]
    )
