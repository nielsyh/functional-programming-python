def filter_odd_numbers(numbers: list[int]) -> list[int]:
    res = []
    for num in numbers:
        if num % 2 != 0:
            res.append(num)
    return res


def filter_odd_numbers_functional(numbers: list[int]) -> list[int]:
    # Using filter and lambda function
    return list(filter(lambda x: x % 2 != 0, numbers))


def filter_odd_numbers_comprehension(numbers: list[int]) -> list[int]:
    # Using list comprehension
    return [x for x in numbers if x % 2 != 0]


# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
expected_output = [1, 3, 5, 7, 9]
assert filter_odd_numbers(numbers_list) == expected_output, "Failed: Incorrect odd number filtering"
assert filter_odd_numbers_functional(numbers_list) == expected_output, "Failed: Incorrect odd number filtering using declarative"
assert filter_odd_numbers_comprehension(numbers_list) == expected_output, "Failed: Incorrect odd number filtering using comprehension"
