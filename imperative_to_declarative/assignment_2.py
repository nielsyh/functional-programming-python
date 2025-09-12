def double_list_imperative(nums: list[int]) -> list[int]:
    """
    # TODO recreate this function declarative style
    """
    for i in range(len(nums)):
        nums[i] = nums[i] * 2
    return nums

    # return list(map(lambda x: x * 2, nums))


# Tests

original = [1, 2, 3]
assert double_list_imperative(original) == [2, 4, 6]

# Test with an empty list
empty_list = []
double_list_imperative(empty_list)
assert empty_list == [], "Failed: Empty list should remain empty"

print("\nAll tests passed!")
