from inspect import signature


def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:  # no space were found
        end = len(text)

    return text[:end].rstrip()


if __name__ == '__main__':
    """
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    print(set(dir(clip.__code__)) - set(dir(object)), indent=10)
    """

    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print("{0} : {1} = {2}".format(
            param.kind,
            name,
            param.default
        ))