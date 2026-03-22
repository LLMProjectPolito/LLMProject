# STEP 1: REASONING
# The function `order_by_points` sorts a list of integers based on the sum of their digits.
# If two numbers have the same digit sum, their original order is preserved.
# We need to test various scenarios:
# - Empty list
# - List with positive numbers
# - List with negative numbers
# - List with a mix of positive and negative numbers
# - Numbers with the same digit sum
# - Single element list
# - Larger lists to test performance and correctness with more data.
# We will use pytest to write unit tests for this function.

# STEP 2: PLAN
# 1. test_empty_list: Test with an empty list.
# 2. test_positive_numbers: Test with a list of positive numbers.
# 3. test_negative_numbers: Test with a list of negative numbers.
# 4. test_mixed_numbers: Test with a list of mixed positive and negative numbers.
# 5. test_same_digit_sum: Test with numbers having the same digit sum.
# 6. test_single_element: Test with a list containing a single element.
# 7. test_larger_list: Test with a larger list to ensure scalability.
# 8. test_zeroes: Test with a list containing zeroes.
# 9. test_large_numbers: Test with large numbers to check digit sum calculation.

# STEP 3: CODE
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
    def digit_sum(n):
        s = 0
        for digit in str(abs(n)):
            s += int(digit)
        return s

    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))

def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_numbers():
    assert order_by_points([1, -11, 2, -22]) == [1, -11, 2, -22]

def test_same_digit_sum():
    assert order_by_points([1, 10, 19, 28]) == [1, 10, 19, 28]

def test_single_element():
    assert order_by_points([5]) == [5]

def test_larger_list():
    assert order_by_points([1, 11, -1, -11, -12, 2, 22, -2, -22]) == [-1, -11, 1, -12, -2, 2, 11, -22, 22]

def test_zeroes():
    assert order_by_points([0, 10, 00, 100]) == [0, 0, 10, 100]

def test_large_numbers():
    assert order_by_points([12345, 6789, 100000, 99999]) == [100000, 12345, 6789, 99999]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]