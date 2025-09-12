def factorial(n: int) -> int:
    """
    # Imperative function for factorial.
    # TODO recreate this function declarative style
    # Think recursive
    # What are the edge/ tail cases?

    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

    # return n * factorial(n - 1)


# Tests
if __name__ == "__main__":
    # Test basic cases
    assert factorial(5) == 120, "Failed: 5! should be 120"
    assert factorial(0) == 1, "Failed: 0! should be 1"
    assert factorial(1) == 1, "Failed: 1! should be 1"
    assert factorial(3) == 6, "Failed: 3! should be 6"

    # Test error handling
    try:
        factorial(-1)
        assert False, "Failed: Should raise ValueError for negative input"
    except ValueError:
        pass  # Expected

    print("All tests passed!")