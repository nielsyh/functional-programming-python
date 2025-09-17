# Functional Programming Exercise: Sales Data Analysis
# Complete implementation with solutions, tests, and type hints

from functools import reduce
from typing import List, Tuple

# Type alias for sales data
SaleItem = Tuple[str, float, int, str]  # (product_name, price, quantity, category)
SalesData = List[SaleItem]

# Sample sales data: each sale is (product_name, price, quantity, category)
sales_data: SalesData = [
    ("Laptop", 999.99, 2, "Electronics"),
    ("Coffee Mug", 12.50, 5, "Home"),
    ("Smartphone", 699.99, 1, "Electronics"),
    ("Book", 24.99, 3, "Education"),
    ("Tablet", 399.99, 1, "Electronics"),
    ("Desk Chair", 149.99, 2, "Home"),
    ("Headphones", 79.99, 4, "Electronics"),
    ("Notebook", 8.99, 10, "Education"),
    ("Monitor", 299.99, 1, "Electronics"),
    ("Lamp", 45.50, 3, "Home")
]


# EXERCISE 1: Basic filtering and mapping
# Use filter and map to find all Electronics items and calculate their total value (price * quantity)
def exercise_1(sales_data: SalesData) -> List[float]:
    electronics = filter(lambda x: x[3] == "Electronics", sales_data)
    return list(map(lambda x: x[1] * x[2], electronics))


# EXERCISE 2: Complex filtering with reduce
# Use filter to get items with quantity > 2, then use reduce to find the total revenue
def exercise_2(sales_data: SalesData) -> float:
    high_quantity = filter(lambda x: x[2] > 2, sales_data)
    return reduce(lambda acc, x: acc + (x[1] * x[2]), high_quantity, 0.0)


# EXERCISE 3: Combining all three functions
# 1. Filter items that cost more than $50
# 2. Map to get just the total value (price * quantity) for each
# 3. Use reduce to sum all values
def exercise_3(sales_data: SalesData) -> float:
    expensive_items = filter(lambda x: x[1] > 50, sales_data)
    values = map(lambda x: x[1] * x[2], expensive_items)
    return reduce(lambda acc, x: acc + x, values, 0.0)


# EXERCISE 4: Category analysis (Advanced)
# Create a function that takes a category name and returns the average item value in that category
def average_value_by_category(sales_data: SalesData, category: str) -> float:
    category_items = filter(lambda x: x[3] == category, sales_data)
    values: List[float] = list(map(lambda x: x[1] * x[2], category_items))
    if not values:
        return 0.0
    return reduce(lambda acc, x: acc + x, values, 0.0) / len(values)


# EXERCISE 5: Challenge - Most valuable category
# Find which category has the highest total revenue using functional programming
def most_valuable_category(sales_data: SalesData) -> str:
    categories = set(map(lambda x: x[3], sales_data))
    category_totals = map(
            lambda cat: (cat, reduce(
                    lambda acc, x: acc + (x[1] * x[2]),
                    filter(lambda x: x[3] == cat, sales_data),
                    0.0
            )),
            categories
    )
    return reduce(lambda max_cat, current: current if current[1] > max_cat[1] else max_cat, category_totals)[0]


# BONUS EXERCISES: More advanced functional programming patterns

# EXERCISE 6: Product analysis
# Find the most expensive single item (highest price * quantity) using functional programming
def most_expensive_item(sales_data: SalesData) -> Tuple[str, float]:
    item_values = map(lambda x: (x[0], x[1] * x[2]), sales_data)
    return reduce(
            lambda max_item, current: current if current[1] > max_item[1] else max_item,
            item_values
    )


# EXERCISE 7: Statistical analysis
# Calculate the median total value across all items using functional programming
def median_item_value(sales_data: SalesData) -> float:
    values: List[float] = sorted(map(lambda x: x[1] * x[2], sales_data))
    n: int = len(values)
    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    else:
        return values[n // 2]


# EXERCISE 8: Multi-criteria filtering
# Find items that are either Electronics over $300 OR Home items with quantity > 3
def complex_filter(sales_data: SalesData) -> List[Tuple[str, float]]:
    filtered_items = filter(
            lambda x: (x[3] == "Electronics" and x[1] > 300) or (x[3] == "Home" and x[2] > 3),
            sales_data
    )
    return list(map(lambda x: (x[0], x[1] * x[2]), filtered_items))


# Run all exercises and tests
def run_tests() -> None:
    print("🚀 Running Functional Programming Tests\n")

    # Helper function to calculate expected values for verification
    def calculate_expected_values() -> None:
        """Calculate and display the actual expected values for verification"""
        print("📊 Calculating expected values for verification:")

        # Exercise 2: Items with quantity > 2
        high_qty_items = [item for item in sales_data if item[2] > 2]
        print(f"Items with quantity > 2: {[(item[0], item[1], item[2]) for item in high_qty_items]}")
        total = sum(item[1] * item[2] for item in high_qty_items)
        print(f"Exercise 2 expected total: {total}")
        print()

    # Calculate and show expected values first
    calculate_expected_values()

    # Test Exercise 1
    result1: List[float] = exercise_1(sales_data)
    expected1: List[float] = [1999.98, 699.99, 399.99, 319.96, 299.99]
    assert result1 == expected1, f"Exercise 1 failed: got {result1}, expected {expected1}"
    print("✓ Exercise 1 - Electronics values:", result1)

    # Test Exercise 2 (corrected expected value)
    result2: float = exercise_2(sales_data)
    expected2: float = 683.83  # Corrected: Coffee Mug (62.5) + Book (74.97) + Headphones (319.96) + Notebook (89.9) + Lamp (136.5)
    assert abs(result2 - expected2) < 0.01, f"Exercise 2 failed: got {result2}, expected {expected2}"
    print("✓ Exercise 2 - High quantity revenue:", round(result2, 2))

    # Test Exercise 3
    result3: float = exercise_3(sales_data)
    expected3: float = 4019.89
    assert abs(result3 - expected3) < 0.01, f"Exercise 3 failed: got {result3}, expected {expected3}"
    print("✓ Exercise 3 - Expensive items total:", round(result3, 2))

    # Test Exercise 4
    result4: float = average_value_by_category(sales_data, "Electronics")
    expected4: float = 743.982
    assert abs(result4 - expected4) < 0.01, f"Exercise 4 failed: got {result4}, expected {expected4}"
    print("✓ Exercise 4 - Electronics average:", round(result4, 2))

    # Test other categories
    home_avg: float = average_value_by_category(sales_data, "Home")
    education_avg: float = average_value_by_category(sales_data, "Education")
    print(f"  • Home category average: {round(home_avg, 2)}")
    print(f"  • Education category average: {round(education_avg, 2)}")

    # Test Exercise 5
    result5: str = most_valuable_category(sales_data)
    expected5: str = "Electronics"
    assert result5 == expected5, f"Exercise 5 failed: got {result5}, expected {expected5}"
    print("✓ Exercise 5 - Most valuable category:", result5)

    # Test empty category
    empty_result: float = average_value_by_category(sales_data, "NonExistent")
    assert empty_result == 0, f"Empty category test failed: got {empty_result}, expected 0"
    print("✓ Empty category test passed")

    print("\n🎯 Bonus Exercises:")

    # Test Exercise 6
    most_expensive: Tuple[str, float] = most_expensive_item(sales_data)
    print("✓ Exercise 6 - Most expensive item:", most_expensive)

    # Test Exercise 7
    median_value: float = median_item_value(sales_data)
    print("✓ Exercise 7 - Median item value:", round(median_value, 2))

    # Test Exercise 8
    complex_items: List[Tuple[str, float]] = complex_filter(sales_data)
    print("✓ Exercise 8 - Complex filter results:", complex_items)

    print("\n🎉 All tests passed! Functional programming mastery achieved!")




if __name__ == "__main__":
    run_tests()

