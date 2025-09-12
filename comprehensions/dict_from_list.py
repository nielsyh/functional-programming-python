# Problem: Given two lists, create a dictionary that maps each key to its corresponding value.
# only use a coperhension to solve this exercise.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = {keys[i]: values[i] for i in range(len(keys))}

# Test
assert my_dict == {'a': 1, 'b': 2, 'c': 3}

print("Exercise passed!")