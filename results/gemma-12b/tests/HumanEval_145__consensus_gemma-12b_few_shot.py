
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
from your_module import order_by_points  # Replace your_module

def sum_digits(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

@pytest.fixture
def sample_list():
    return [1, 11, -1, -11, -12]

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def single_element_list():
    return [5]

@pytest.fixture
def list_with_zeros():
    return [0, 10, 100, -10]

@pytest.fixture
def list_with_negative_and_positive():
    return [-5, 5, -10, 10, 15, -15]

def test_order_by_points_sample(sample_list):
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_list) == expected

def test_order_by_points_empty(empty_list):
    assert order_by_points(empty_list) == []

def test_order_by_points_single_element(single_element_list):
    assert order_by_points(single_element_list) == single_element_list

def test_order_by_points_with_zeros(list_with_zeros):
    expected = [0, -10, 10, 100]
    assert order_by_points(list_with_zeros) == expected

def test_order_by_points_negative_and_positive(list_with_negative_and_positive):
    expected = [-5, 5, -10, 10, -15, 15]
    assert order_by_points(list_with_negative_and_positive) == expected

def test_order_by_points_same_digit_sum():
    nums = [12, 3, 21, 4]
    expected = [3, 4, 12, 21]
    assert order_by_points(nums) == expected

def test_order_by_points_large_numbers():
    nums = [123, 45, 6, 789, 10]
    expected = [10, 6, 45, 123, 789]
    assert order_by_points(nums) == expected

def test_order_by_points_all_negative():
    nums = [-1, -2, -3, -4, -5]
    expected = [-1, -2, -3, -4, -5]
    assert order_by_points(nums) == expected

def test_order_by_points_mixed_signs_same_sum():
    nums = [1, -1, 10, -10, 11, -11]
    expected = [1, -1, 10, -10, 11, -11]
    assert order_by_points(nums) == expected