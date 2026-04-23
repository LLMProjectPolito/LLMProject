
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
STEP 1: REASONING -
The function `order_by_points` sorts a list of integers based on the sum of their digits. If two numbers have the same sum of digits, they should be sorted based on their original index in the input list.
The edge case is an empty list, which should return an empty list.
We need to test various scenarios including positive numbers, negative numbers, zero, empty list, and lists with numbers having the same digit sum.

STEP 2: PLAN -
Test functions:
1.  `test_empty_list`: Checks if an empty list returns an empty list.
2.  `test_positive_numbers`: Checks sorting with positive numbers.
3.  `test_negative_numbers`: Checks sorting with negative numbers.
4.  `test_mixed_numbers`: Checks sorting with a mix of positive and negative numbers.
5.  `test_same_digit_sum`: Checks sorting when numbers have the same digit sum.
6.  `test_zero`: Checks sorting with zero.

STEP 3: CODE -