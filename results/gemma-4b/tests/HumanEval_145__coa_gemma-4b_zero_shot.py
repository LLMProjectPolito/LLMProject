
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
import math


# Focus: Boundary Values
import pytest

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]

# Focus: Type Scenarios
import pytest

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element_positive():
    assert order_by_points([5]) == [5]

def test_single_element_negative():
    assert order_by_points([-5]) == [-5]

# Focus: Logic Branches
import pytest

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_sum():
    assert order_by_points([1, 11, 12, 111]) == [1, 11, 111, 12]