import keyword
from collections import abc


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object using attribute notation"""

    def __new__(cls, arg):  # As a class method, the first argument __new__ gets is the class itself, and the remaining arguments are the same that __init__ gets, except for self.
        if isinstance(arg, abc.Mapping):
            return super().__new__(
                cls)  # The default behavior is to delegate to the __new__ of a super calss. In this case , we are calling __new__ from the obect base c lass, passing FrozenJSON as the only argument
        elif isinstance(arg, abc.MutableSequence):  # The remaining lines of __new__ are exactly as in the old build method
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])
