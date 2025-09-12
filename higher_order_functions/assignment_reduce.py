from typing import Callable, List, Union
from functools import reduce


# Helper functions
def add_all(numbers: List[Union[int, float]]) -> Union[int, float]:
    return sum(numbers)


def multiply_all(numbers: List[Union[int, float]]) -> Union[int, float]:
    # TODO: Implement this function to multiply all numbers in the list with reduce.
    return reduce(lambda x, y: x * y, numbers, 1)


# Declarative Solution (User's Task)
def execute_operation(numbers: List[Union[int, float]],
                      operation: Callable[[List[Union[int, float]]], Union[int, float]]) -> Union[int, float]:
    """
    Executes a mathematical operation on a list of numbers.

    Args:
        numbers: A list of numbers.
        operation: The function object to be executed.

    Returns:
        The result of the operation.
    """
    # TODO: Implement this function by directly calling the `operation` function
    return operation(numbers)


# Test cases
data = [1, 2, 3, 4, 5]

# Pass the `add_all` function object directly as an argument
add_result = execute_operation(data, add_all)
assert add_result == 15

# Pass the `multiply_all` function object directly
# The `multiply_all` function must be implemented first.
multiply_result = execute_operation(data, multiply_all)
assert multiply_result == 120

print("`execute_operation` solution passed all tests!")
