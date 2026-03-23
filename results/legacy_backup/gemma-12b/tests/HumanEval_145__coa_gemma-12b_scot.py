import pytest
import math


# Focus: Boundary Values
def test_order_by_points_empty_list():
    """Test with an empty list - boundary condition."""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test with a single element list - boundary condition."""
    assert order_by_points([5]) == [5]

def test_order_by_points_all_negative():
    """Test with all negative numbers - boundary condition."""
    assert order_by_points([-1, -2, -3]) == [-1, -2, -3]

# Focus: Type Scenarios
def test_order_by_points_empty_list():
    """Test with an empty list."""
    assert order_by_points([]) == []

def test_order_by_points_positive_and_negative_numbers():
    """Test with a mix of positive and negative numbers."""
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_numbers_with_same_digit_sum():
    """Test with numbers having the same digit sum, preserving original order."""
    assert order_by_points([12, 21, 3]) == [3, 12, 21]

# Focus: Logic Branches
def test_order_by_points_positive_and_negative_numbers():
    nums = [1, 11, -1, -11, -12]
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == expected

def test_order_by_points_empty_list():
    nums = []
    expected = []
    assert order_by_points(nums) == expected

def test_order_by_points_same_digit_sum():
    nums = [12, 3, 21]
    expected = [3, 12, 21]
    assert order_by_points(nums) == expected