
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

import pytest

# Implementation Note:
# The function 'order_by_points' is expected to:
# 1. Calculate the sum of the absolute digits of each number.
# 2. Sort numbers primarily by this sum in ascending order.
# 3. Maintain original relative order for ties (stable sort).
# 4. Not mutate the original input list.

@pytest.mark.parametrize("input_list, expected_output", [
    # --- Basic Scenarios ---
    ([], []),                                      # Case: Empty list
    ([42], [42]),                                  # Case: Single element
    ([1, 2, 3, 10], [1, 10, 2, 3]),                # Case: Basic sorting (Sums: 1, 1, 2, 3)
    ([30, 1, 2], [1, 2, 30]),                      # Case: Simple ascending sums
    
    # --- Stability (Tie-breaking using original index) ---
    ([10, 1, 100], [10, 1, 100]),                  # Case: Same sum (1), maintain order
    ([22, 13, 4], [22, 13, 4]),                    # Case: Same sum (4), maintain order
    ([20, 11, 2, 101], [20, 11, 2, 101]),          # Case: Same sum (2), maintain order
    
    # --- Negative Numbers (Digit sum uses absolute value) ---
    ([-1, -11, -12, 1], [-1, 1, -11, -12]),        # Case: Mixed signs (Sums: 1, 2, 3, 1)
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]),# Case: Complex mixed signs
    ([-9, -1, 10], [-1, 10, -9]),                  # Case: Negatives with large digit sums
    ([-5, 5, 14], [-5, 5, 14]),                    # Case: Negatives vs Positives (all sum to 5)
    
    # --- Zero Handling ---
    ([1, 0, -1], [0, 1, -1]),                      # Case: Zero (sum 0) comes first
    
    # --- Large Numbers ---
    ([999, 100, 1], [1, 100, 999]),                # Case: Large digit sums
    ([99, 11, 1000000], [1000000, 11, 99]),        # Case: Large magnitude, small sum
    
    # --- Complex Mixes ---
    ([15, 2, 4, 10, 21], [10, 2, 21, 4, 15]),      # Case: Mixed variety
    ([55, 19, 2, -2, 101], [2, -2, 101, 55, 19]),  # Case: High complexity mix
])
def test_order_by_points_logic(input_list, expected_output):
    """
    Tests the core logic: ascending sum of digits, then original index (stability).
    Covers empty, single, sorted, stability, negatives, zero, and large numbers.
    """
    from your_module import order_by_points  # Replace with actual import
    assert order_by_points(input_list) == expected_output


def test_order_by_points_immutability():
    """
    Ensures that the function does not mutate (change) the original input list.
    A common bug in sorting functions is using .sort() instead of sorted().
    """
    from your_module import order_by_points
    original = [10, 1, 2]
    input_list = list(original)  # Create a copy to pass in
    order_by_points(input_list)
    assert input_list == original, "The function should not modify the original input list"