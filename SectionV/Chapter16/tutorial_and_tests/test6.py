"""
When a generator >gen< calls >yield from subgen()<, the >subgen< takes over an will yield values to the caller of
>gen<; the caller will in effect drive >subgen< directly.

The main feature of >yield from< is to open a bidirectional channel from the outermost caller to the innermost subgenerator,
so that values can be sent and yielded back and forth directly from them, and exceptions can be thrown all the way in
without adding a lot of exception handling boilerplate code in the intermediate coroutines.

This enables coroutine delegation
"""
from collections import namedtuple

Result = namedtuple("Result", "count average")


def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        new_value = yield average

        if new_value is None:
            break

        total += new_value
        count += 1
        average = total / count

    return Result(count, average)


def get_average_for_list_of_values(result_dict, dict_key):
    while True:
        result_dict[dict_key] = yield from averager()


def main():
    data = {
        "key1": [50, 100],
        "key2": [0, 100],
    }
    """
    result: {
        "key1": Result(2, 75.0), # using namedtuple Result
        "key2": Result(2, 50.0), # using namedtuple Result
    } 
    """

    result = {}
    for key, list_of_values in data.items():
        get_average_for_list_of_values_delegating_generator = get_average_for_list_of_values(result,
                                                                                             key)  # already primed
        next(get_average_for_list_of_values_delegating_generator)

        for value in list_of_values:
            get_average_for_list_of_values_delegating_generator.send(
                value  # value sent to the innermost subgen
            )

        get_average_for_list_of_values_delegating_generator.send(None)  # Close the innermost subgen

    print(result)


if __name__ == '__main__':
    main()
