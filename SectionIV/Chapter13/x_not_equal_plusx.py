def main1():
    import decimal

    ctx = decimal.getcontext()  # Get a reference to the current global arithmetic context
    ctx.prec = 40  # Set the precision of the arithmetic context to 40

    one_third = decimal.Decimal('1') / decimal.Decimal('3')  # Computer 1/3 using the current precision
    print(one_third)  # Inspect the result; there are 40 digits after the decimal point.

    print(one_third == +one_third)  # one_third == +one_third is True

    ctx.prec = 28  # Lower precision to 28 - the default for Decimal arithmetic in Python 3.4

    print(one_third == +one_third)  # Now one_third == +one_third is False

    print(+one_third)  # Inspect +one_third; there are 28 digits after the '.' here.


def main2():
    from collections import Counter

    ct = Counter("abracadabra")
    print(ct)
    ct['r'] = -3
    ct['d'] = 0
    print(ct)
    print(+ct)


if __name__ == '__main__':
    main2()
