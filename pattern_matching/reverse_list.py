from typing import Iterable


def reverse(lst: Iterable) -> Iterable:
    match lst:
        case [x, *xs]:
            return reverse(xs) + [x]
        case _:
            return []
        

assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse([]) == []
assert reverse([42]) == [42]
assert reverse([[1, 2], [3, 4], [5, 6]]) == [[5, 6], [3, 4], [1, 2]]
assert reverse((1, 2, 3)) == [3, 2, 1]