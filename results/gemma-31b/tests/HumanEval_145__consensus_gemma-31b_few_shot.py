
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

@pytest.mark.parametrize("nums, expected", [
    # Basic cases
    ([], []),
    ([0], [0]),
    ([10], [10]),
    ([5], [5]),
    # Different sums
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([100, 11, 12], [100, 11, 12]),  # sums: 1, 2, 3
    ([12, 11, 100], [100, 11, 12]),  # sums: 3, 2, 1
    ([99, 10, 11], [10, 11, 99]),    # sums: 18, 1, 2
    ([10, 20, 30], [10, 20, 30]),    # sums: 1, 2, 3
    ([30, 20, 10], [10, 20, 30]),    # sums: 3, 2, 1
    # Stable sort (same sums, maintain original order)
    ([10, 1, 100], [10, 1, 100]),    # all sum to 1
    ([1, 10, 100], [1, 10, 100]),    # all sum to 1
    ([100, 10, 1], [100, 10, 1]),    # all sum to 1
    ([11, 20, 2], [11, 20, 2]),      # all sum to 2
    # Negative numbers
    ([-1, -2, -3], [-1, -2, -3]),    # sums: 1, 2, 3
    ([-3, -2, -1], [-1, -2, -3]),    # sums: 3, 2, 1
    ([-10, -1], [-10, -1]),          # both sum to 1, stable
    ([-1, -10], [-1, -10]),          # both sum to 1, stable
    ([-10, -1, -100], [-10, -1, -100]), # all sum to 1, stable
    # Mixed positive and negative
    ([1, -1], [1, -1]),              # both sum to 1, stable
    ([-1, 1], [-1, 1]),              # both sum to 1, stable
    ([11, -2, 20], [11, -2, 20]),    # all sum to 2, stable
    ([11, -1, 2], [-1, 11, 2]),      # sums: 2, 1, 2 -> sorted: -1(1), 11(2), 2(2)
    ([1, 11, -1, -11, -12], [1, -1, 11, -11, -12]), # sums: 1, 2, 1, 2, 3 -> stable sort
    # Large numbers
    ([999, 1000], [1000, 999]),      # sums: 27, 1
    ([999, 1000, 123], [1000, 123, 999]), # sums: 27, 1, 6
    ([12345, 54321], [12345, 54321]),# both sum to 15, stable
    # Zeros
    ([0, 0, 0], [0, 0, 0]),
    ([10, 0, 1], [0, 10, 1]),        # sums: 1, 0, 1 -> sorted: 0(0), 10(1), 1(1)
    ([0, 1, 0], [0, 0, 1]),          # sums: 0, 1, 0 -> sorted: 0(0), 0(0), 1(1)
])
def test_order_by_points(nums, expected):
    """
    Tests that order_by_points sorts integers by the sum of their digits
    while maintaining stability for items with the same sum.
    """
    assert order_by_points(nums) == expected

def test_order_by_points_stability_explicit():
    """
    Explicitly test stability with a larger set of identical sums.
    """
    # All these numbers have a digit sum of 2
    nums = [11, 2, 20, 101, 110, -2, -11, -20]
    assert order_by_points(nums) == nums

    # All these numbers have a digit sum of 1
    nums_one = [10, 1, 100, -1, -10, -100]
    assert order_by_points(nums_one) == nums_one

def test_order_by_points_large_range():
    """
    Test with a wide range of values to ensure robustness.
    """
    nums = [10**9, 1, 10**9 - 1] # Sums: 1, 1, 81
    expected = [10**9, 1, 10**9 - 1] # Stable sort for 10^9 and 1
    assert order_by_points(nums) == expected