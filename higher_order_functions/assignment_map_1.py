from typing import Callable, List, Union


# Imperative Solution (Provided for comparison)
def apply_operation_imperative(numbers: List[Union[int, float]], operation_name: str) -> List[Union[int, float]]:
    """Applies an operation to a list of numbers based on a string name."""
    results: List[Union[int, float]] = []
    if operation_name == 'double':
        for num in numbers:
            results.append(num * 2)
    elif operation_name == 'square':
        for num in numbers:
            results.append(num ** 2)
    return results


# Helper functions to be passed as arguments
def double(x: Union[int, float]) -> Union[int, float]:
    return x * 2


def square(x: Union[int, float]) -> Union[int, float]:
    return x ** 2


# Declarative Solution (User's Task)
def apply_operation_declarative(numbers: List[int],
                                operation: Callable[[int], int]) -> List[int]:
    """
    Applies a given function to each number in a list.

    Args:
        numbers: A list of numbers (integers or floats).
        operation: A function that takes a single number and returns a number.

    Returns:
        A new list containing the results of applying the operation to each number.
    """

    return list(map(operation, numbers))


# Test cases for the user's implementation
numbers_list = [1, 2, 3, 4]

# Pass the `double` function as an argument
doubled_result = apply_operation_declarative(numbers_list, double)
assert doubled_result == [2, 4, 6, 8]

# Pass the `square` function as an argument
squared_result = apply_operation_declarative(numbers_list, square)
assert squared_result == [1, 4, 9, 16]

print("Declarative solution passed all tests!")
