import pytest
import math


# Focus: Boundary Values
import pytest

def sum_digits(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

def test_order_by_points_empty_list():
    nums = []
    expected = []
    assert order_by_points(nums) == expected

def test_order_by_points_single_element():
    nums = [5]
    expected = [5]
    assert order_by_points(nums) == expected

def test_order_by_points_boundary_zero():
    nums = [0, 1, -1]
    expected = [0, -1, 1]
    assert order_by_points(nums) == expected

# Focus: Type Scenarios
def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_positive_and_negative_numbers():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_numbers_with_same_digit_sum():
    assert order_by_points([12, 21, 3]) == [3, 12, 21]

# Focus: Logic Branches
import pytest

def sum_digits(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_positive_and_negative_numbers():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_digit_sum():
    assert order_by_points([12, 21, 3]) == [3, 12, 21]