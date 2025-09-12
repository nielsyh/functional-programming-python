# Problem: Create a list containing only the even numbers from a given list.
# only use a coperhension to solve this exercise.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]

# Test
assert evens == [2, 4, 6, 8, 10]

print("Exercise passed!")