
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
    """Helper function to calculate the sum of digits of a number."""
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

def test_order_by_points_sample(sample_list):
    assert order_by_points(sample_list) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty(empty_list):
    assert order_by_points(empty_list) == []

def test_order_by_points_single_element(single_element_list):
    assert order_by_points(single_element_list) == single_element_list

def test_order_by_points_with_zeros(list_with_zeros):
    assert order_by_points(list_with_zeros) == [0, -10, 10, 100]

def test_order_by_points_zero_sums():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]
    assert order_by_points([-10, 10]) == [-10, 10]

def test_order_by_points_invalid_input():
    with pytest.raises(TypeError):
        order_by_points(["a", 1, 2])

def test_order_by_points_mixed_data_types():
    assert order_by_points([1, 1.5, 2]) == [1, 1.5, 2]

def test_order_by_points_large_digit_sums():
    assert order_by_points([999999999, 1, 10]) == [1, 10, 999999999]

def test_order_by_points_with_same_digit_sum(list_with_same_digit_sum):
    assert order_by_points(list_with_same_digit_sum) == [1, 10, 100, 1000]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 6, 789]) == [6, 45, 123, 789]

def test_order_by_points_mixed_positive_negative_large():
    assert order_by_points([-123, 45, -6, 789]) == [-6, -123, 45, 789]

def test_order_by_points_all_negative():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_all_positive():
    assert order_by_points([1, 10, 100]) == [1, 10, 100]

def test_order_by_points_duplicate_numbers():
    assert order_by_points([1, 1, 1]) == [1, 1, 1]

def test_order_by_points_duplicate_numbers_with_different_sums():
    assert order_by_points([1, 10, 1, 100]) == [1, 1, 10, 100]

def test_order_by_points_stability():
    nums = [1, 11, -1, -11, -12]
    result1 = order_by_points(nums)
    result2 = order_by_points(nums)
    assert result1 == result2

def test_order_by_points_with_leading_zeros():
    assert order_by_points([1, 2, 10, 20]) == [1, 2, 10, 20]