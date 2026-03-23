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
    if not nums:
        return []

    def sum_digits(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s

    nums_with_index = list(enumerate(nums))
    nums_with_index.sort(key=lambda x: (sum_digits(x[1]), x[0]))
    return [num for _, num in nums_with_index]

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
    if not nums:
        return []

    def sum_digits(n):
        s = 0
        for digit in str(n):
            s += int(digit)
        return s

    nums_with_index = list(enumerate(nums))
    nums_with_index.sort(key=lambda x: (sum_digits(x[1]), x[0]))
    return [num for _, num in nums_with_index]