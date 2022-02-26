from pprint import pprint
from random import shuffle
from typing import List

from comparator import FunctionsTimer


def sorted_sol():
    a = [7, 3, 2, 5, 1, 4, 9, 8, 6]
    shuffle(a)

    a = sorted(a)
    return a == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def set_sol():

    a = [7, 3, 2, 5, 1, 4, 9, 8, 6]
    shuffle(a)

    a = set(a)
    return a == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def sorted_with_params(a: List[int]):
    shuffle(a)

    a = sorted(a)
    return a == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def set_with_params(a: List[int]):
    shuffle(a)

    a = set(a)
    return a == {1, 2, 3, 4, 5, 6, 7, 8, 9}


def main():

    ft = FunctionsTimer()

    # example with function without params
    times = ft.time_funcs(
        {
            sorted_sol: {},
            set_sol: {},
        },
        repeat_times=2,  # optional
        num_trials=1_000_000,  # optional
    )
    print("Example function without params")
    pprint(times)
    print()
    # example with function with params
    times = ft.time_funcs(
        {
            sorted_with_params: {"a": [1, 2, 3, 4, 5]},
            set_with_params: {"a": [1, 2, 3, 4, 5]},
        },
        repeat_times=2,  # optional
        num_trials=1_000_000,  # optional
    )
    print("Example function with params")
    pprint(times)

    print("\nAccessing different object attributes:")

    print("\ncode_times")
    print(ft.code_times)
    print("\nfuncs_code_times")
    print(ft.funcs_code_times)
    print("\nfuncs_times")
    print(ft.funcs_times)


if __name__ == "__main__":
    main()
