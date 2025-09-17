def celsius_to_fahrenheit_imperative(celsius_temps: list[int | float]) -> list[float]:
    res = []
    for c in celsius_temps:
        res.append(c * 9 / 5 + 32)
    return res


def celsius_to_fahrenheit_coph(celsius_temps: list[int | float]) -> list[float]:
    # implement using list comprehension
    pass


def celsius_to_fahrenheit_decl(celsius_temps: list[int | float]) -> list[float]:
    # implement using map and lambda
    pass


celsius_list = [0, 20, 37, 100]


assert celsius_to_fahrenheit_imperative(celsius_list) == [32.0, 68.0, 98.6, 212.0], "Failed: Incorrect conversion to Fahrenheit"
assert celsius_to_fahrenheit_coph(celsius_list) == [32.0, 68.0, 98.6, 212.0], "Failed: Incorrect conversion to Fahrenheit using comprehension"
assert celsius_to_fahrenheit_decl(celsius_list) == [32.0, 68.0, 98.6, 212.0], "Failed: Incorrect conversion to Fahrenheit using map"
