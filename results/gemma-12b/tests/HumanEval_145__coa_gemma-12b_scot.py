
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
def test_boundary_empty_list():
    assert order_by_points([]) == []

def test_boundary_single_element():
    assert order_by_points([5]) == [5]

def test_boundary_negative_and_positive_zero():
    assert order_by_points([0, -0]) == [0, -0]

# Focus: Type Scenarios
def test_type_scenario_empty_list():
    assert order_by_points([]) == []

def test_type_scenario_positive_and_negative_numbers():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_type_scenario_mixed_types_raises_typeerror():
    try:
        order_by_points([1, "a", 2])
        assert False, "TypeError not raised"
    except TypeError:
        assert True

# Focus: Logic Branches
def test_order_by_points_positive_and_negative():
    nums = [1, 11, -1, -11, -12]
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == expected

def test_order_by_points_empty_list():
    nums = []
    expected = []
    assert order_by_points(nums) == expected

def test_order_by_points_same_digit_sum():
    nums = [12, 21, 3]
    expected = [3, 12, 21]
    assert order_by_points(nums) == expected