from typing import Iterable


def length(lst: Iterable) -> int:
    # TODO: Implement this function using pattern matching to calculate the length of the list.
    # TODO: hint use recursion lst[_, *xs]
    pass


test_list = [1, 2, 3, 4, 5]

assert length(test_list) == 5, "Failed: Length should be 5"
assert length([]) == 0, "Failed: Length of empty list should be 0"