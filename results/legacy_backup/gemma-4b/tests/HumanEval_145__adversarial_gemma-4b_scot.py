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
# We need to test various scenarios including empty lists, positive numbers, negative numbers, and numbers with different digit sums.
# We also need to verify that the sorting is done correctly according to the problem description.

# STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with positive numbers: [1, 11, 2, 3]
# 3. List with negative numbers: [-1, -11, -2, -3]
# 4. List with mixed positive and negative numbers: [1, -1, 11, -11]
# 5. List with numbers having the same digit sum: [1, 11, 10, 100]
# 6. List with zero: [0, 1, 10]
# 7. List with large numbers: [123, 45, 6]

# Test function names:
# test_empty_list
# test_positive_numbers
# test_negative_numbers
# test_mixed_numbers
# test_same_digit_sum
# test_zero
# test_large_numbers


# STEP 3: CODE
# pytest suite
def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 3]) == [1, 2, 3, 11]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -3]) == [-1, -2, -3, -11]

def test_mixed_numbers():
    assert order_by_points([1, -1, 11, -11]) == [-1, 1, -11, 11]

def test_same_digit_sum():
    assert order_by_points([1, 11, 10, 100]) == [1, 10, 100, 11]

def test_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_large_numbers():
    assert order_by_points([123, 45, 6]) == [6, 45, 123]