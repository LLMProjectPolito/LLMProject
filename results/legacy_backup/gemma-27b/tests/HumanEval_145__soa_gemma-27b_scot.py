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
# Edge cases include empty lists, lists with only positive numbers, lists with only negative numbers,
# and lists with a mix of positive and negative numbers.  The digit sum calculation needs to handle negative numbers correctly.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests the function with an empty list.
# - test_positive_numbers: Tests with a list of positive numbers.
# - test_negative_numbers: Tests with a list of negative numbers.
# - test_mixed_numbers: Tests with a list of mixed positive and negative numbers.
# - test_same_digit_sum: Tests with numbers having the same digit sum.
# - test_single_element: Tests with a list containing a single element.
# - test_large_numbers: Tests with larger numbers to ensure digit sum calculation works correctly.
# - test_zero: Tests with a list containing zero.
# - test_duplicate_numbers: Tests with duplicate numbers in the input list.

# STEP 3: CODE
def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_numbers():
    assert order_by_points([1, -11, 2, -22]) == [1, -11, 2, -22]

def test_same_digit_sum():
    assert order_by_points([10, 1, 19, 100]) == [1, 10, 19, 100]

def test_single_element():
    assert order_by_points([5]) == [5]

def test_large_numbers():
    assert order_by_points([1234, 567, 89, 10]) == [10, 89, 567, 1234]

def test_zero():
    assert order_by_points([0, 1, -1]) == [0, 1, -1]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 11, 11]) == [1, 1, 11, 11]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_more_complex_case():
    assert order_by_points([21, 12, 3, 30, 10]) == [3, 10, 12, 21, 30]

def test_negative_and_zero():
    assert order_by_points([-10, 0, -1, -11]) == [0, -1, -10, -11]