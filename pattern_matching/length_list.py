from typing import Iterable


def length(lst: Iterable) -> int:
    match lst:
        case [_, *xs]:
            return 1 + length(xs)
        case _:
            return 0


test_list = [1, 2, 3, 4, 5]

assert length(test_list) == 5, "Failed: Length should be 5"
assert length([]) == 0, "Failed: Length of empty list should be 0"