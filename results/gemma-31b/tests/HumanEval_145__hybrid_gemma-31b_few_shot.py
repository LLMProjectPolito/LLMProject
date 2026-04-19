
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

def order_by_points(nums):
    """
    Sorts integers by the sum of their digits (absolute value).
    Maintains original order for identical sums (stable sort).
    """
    def get_digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    
    # Python's sorted() is stable by default.
    return sorted(nums, key=get_digit_sum)

# --- Pytest Suite ---

@pytest.mark.parametrize("input_list, expected", [
    # Edge Cases: Empty and Single Element
    ([], []), 
    ([42], [42]),
    
    # Basic Sorting: Simple ascending digit sums
    ([10, 2, 30], [10, 2, 30]),        # Sums: 1, 2, 3
    ([30, 2, 10], [10, 2, 30]),        # Sums: 3, 2, 1 -> Sorted: 1, 2, 3
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    
    # Negative Number Handling: Treat as absolute values
    ([-12, -11, -1], [-1, -11, -12]),  # Sums: 3, 2, 1 -> Sorted: 1, 2, 3
    ([-11, -1, -2], [-1, -11, -2]),    # Sums: 2, 1, 2 -> Sorted: 1, 2, 2
    
    # Zeros and Large Numbers
    ([0, 10, 0], [0, 0, 10]),          # Sums: 0, 1, 0 -> Sorted: 0, 0, 1
    ([999, 1000, 0], [0, 1000, 999]),  # Sums: 27, 1, 0 -> Sorted: 0, 1, 27
    ([123456789, 1], [1, 123456789]),  # Sums: 45, 1
    
    # Mixed Values: Positive, Negative, and Zeros
    ([15, -20, 11, -1], [-1, -20, 11, 15]), # Sums: 6, 2, 2, 1 -> Sorted: 1, 2, 2, 6
    ([10, -10, 11, -11, 2], [10, -10, 11, -11, 2]), # Sums: 1, 1, 2, 2, 2
])
def test_order_by_points_scenarios(input_list, expected):
    """Tests a wide array of scenarios including edge cases and mixed signs."""
    assert order_by_points(input_list) == expected

def test_order_by_points_stability():
    """
    Explicitly verifies that the sort is stable.
    If multiple numbers have the same digit sum, their original relative order must be preserved.
    """
    # All these numbers have a digit sum of 2
    # Relative order: 11 (idx 0), 20 (idx 1), 2 (idx 2), 101 (idx 3), -11 (idx 4), -2 (idx 5)
    nums = [11, 20, 2, 101, -11, -2]
    result = order_by_points(nums)
    
    assert result == nums, "The sort failed to maintain stability for identical digit sums."

def test_order_by_points_stability_mixed_sums():
    """
    Verifies stability when there are both identical and different sums.
    """
    # Sums: 10(1), 1(1), 100(1), 0(0), -1(1)
    # 0 should move to the front, others should maintain relative order.
    nums = [10, 1, 100, 0, -1]
    expected = [0, 10, 1, 100, -1]
    assert order_by_points(nums) == expected