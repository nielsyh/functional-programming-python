from typing import Iterable


def reverse(lst: Iterable) -> Iterable:
    # TODO: Implement this function using pattern matching to reverse the list.
    # TODO: hint use recursion lst[_, *xs]
    pass
        

assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([]) == []
assert reverse([42]) == [42]
assert reverse([[1, 2], [3, 4], [5, 6]]) == [[5, 6], [3, 4], [1, 2]]
assert reverse((1, 2, 3)) == [3, 2, 1]