
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
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    return sorted(nums, key=lambda x: sum(int(digit) for digit in str(abs(x))))


### SCoT Steps:

# STEP 1: REASONING
# The function `order_by_points` sorts a list of integers based on the sum of their digits.
# If two numbers have the same sum of digits, they should be sorted based on their original index.
# We need to test various scenarios including:
# 1. Empty list: Should return an empty list.
# 2. List with positive numbers: Should sort based on digit sum.
# 3. List with negative numbers: Should sort based on digit sum, considering the absolute value.
# 4. List with mixed positive and negative numbers: Should sort based on digit sum, considering the absolute value.
# 5. List with numbers having the same digit sum: Should maintain the original order.
# 6. List with zero: Should handle zero correctly.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests the case when the input list is empty.
# - test_positive_numbers: Tests the case when the input list contains only positive numbers.
# - test_negative_numbers: Tests the case when the input list contains only negative numbers.
# - test_mixed_numbers: Tests the case when the input list contains both positive and negative numbers.
# - test_same_digit_sum: Tests the case when multiple numbers have the same digit sum.
# - test_with_zero: Tests the case when the input list contains zero.

# STEP 3: CODE
# pytest suite
def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_numbers():
    assert order_by_points([-1, 11, -2, 22]) == [-1, -2, 11, 22]

def test_same_digit_sum():
    assert order_by_points([1, 11, 10, 100]) == [1, 10, 100, 11]

def test_with_zero():
    assert order_by_points([0, 1, 10, -10]) == [-10, 0, 1, 10]