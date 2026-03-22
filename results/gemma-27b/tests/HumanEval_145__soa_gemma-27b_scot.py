import pytest

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
    def sum_digits(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (sum_digits(x), nums.index(x)))

# STEP 1: REASONING
# The function `order_by_points` sorts a list of integers based on the sum of their digits.
# If two numbers have the same digit sum, their original order is preserved.
# Edge cases include an empty list and lists with negative numbers.
# The digit sum calculation needs to handle negative numbers correctly (using absolute value).

# STEP 2: PLAN
# Test cases:
# 1. Empty list: Should return an empty list.
# 2. Basic test case: Example from the problem description.
# 3. List with all same digit sums: Should preserve original order.
# 4. List with negative numbers: Should handle negative numbers correctly.
# 5. List with mixed positive and negative numbers.
# 6. List with zero.
# 7. List with large numbers.
# 8. List with duplicate numbers.

# STEP 3: CODE
def test_empty_list():
    assert order_by_points([]) == []

def test_basic_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sums():
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_mixed_numbers():
    assert order_by_points([1, -1, 10, -10]) == [-1, 1, -10, 10]

def test_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_large_numbers():
    assert order_by_points([12345, 6789, 1, 10]) == [1, 10, 12345, 6789]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 11, 11]) == [1, 1, 11, 11]

def test_more_complex_case():
    assert order_by_points([23, 1, 4, 12, 5]) == [1, 4, 5, 12, 23]

def test_negative_and_positive_with_same_digit_sum():
    assert order_by_points([-11, 2, 11, -2]) == [-11, -2, 2, 11]