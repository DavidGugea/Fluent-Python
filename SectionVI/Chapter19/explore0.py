from collections import abc


class FrozenJSON:
    """A read-only facade for navigating a JSON-like object using attribute notation"""

    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):  # __getattr__ is called only when there's no attribute with that name
        if hasattr(self.__data, name):
            return getattr(self.__data, name)  # if name matches an attribute of the instance __data, return that.
        else:
            return FrozenJSON.build(self.__data[
                                        name])  # Otherwise, fetch the item with the key name from self.__data, and return the result of calling FrozenJSON.build() on that.

    @classmethod
    def build(cls, obj):  # this is an alternate constructor, a common use for the @classmethod decorator
        if isinstance(obj, abc.Mapping):  # if obj is a mapping, built a FrozenJSON with it
            return cls(obj)
        elif isinstance(obj,
                        abc.MutableSequence):  # If it is a MutableSequence, it must be a list, so we built a list by passing every item in obj recursively to .build()
            return [cls.build(item) for item in obj]
        else:  # If it's not a dict or a list return the item as it is
            return obj
