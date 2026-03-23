import pytest
import math


# Focus: Boundary Values
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

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_negative_numbers():
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 11, -11]) == [-1, 1, -11, 11]

# Focus: Type Scenarios
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
    
def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

# Focus: Logic Branches
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
    
def test_empty_list():
    assert order_by_points([]) == []

def test_positive_numbers():
    assert order_by_points([1, 11, 2, 20]) == [1, 2, 11, 20]

def test_negative_numbers():
    assert order_by_points([-1, -11, -2, -20]) == [-1, -2, -11, -20]