
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
def sample_data():
    return [1, 11, -1, -11, -12]

@pytest.fixture
def empty_data():
    return []

@pytest.fixture
def single_element_data():
    return [5]

@pytest.fixture
def multiple_elements_same_digit_sum():
    return [10, 1, 100, 1000]

@pytest.fixture
def negative_and_positive_same_digit_sum():
    return [1, -1, 10, -10]

def test_order_by_points_sample_data(sample_data):
    expected = [-1, -11, 1, -12, 11]
    actual = order_by_points(sample_data)
    assert actual == expected

def test_order_by_points_empty_data(empty_data):
    expected = []
    actual = order_by_points(empty_data)
    assert actual == expected

def test_order_by_points_single_element_data(single_element_data):
    expected = single_element_data
    actual = order_by_points(single_element_data)
    assert actual == expected

def test_order_by_points_multiple_elements_same_digit_sum(multiple_elements_same_digit_sum):
    expected = [1, 10, 100, 1000]
    actual = order_by_points(multiple_elements_same_digit_sum)
    assert actual == expected

def test_order_by_points_negative_and_positive_same_digit_sum(negative_and_positive_same_digit_sum):
    expected = [1, -1, 10, -10]
    actual = order_by_points(negative_and_positive_same_digit_sum)
    assert actual == expected

def test_order_by_points_large_numbers():
    data = [12345, -12345, 6789, -6789]
    expected = [-12345, -6789, 12345, 6789]
    actual = order_by_points(data)
    assert actual == expected

def test_order_by_points_zero():
    data = [0, 1, -1, 10, -10]
    expected = [-1, 1, -10, 10, 0]
    actual = order_by_points(data)
    assert actual == expected

def test_order_by_points_all_negative():
    data = [-1, -2, -3, -4, -5]
    expected = [-1, -2, -3, -4, -5]
    actual = order_by_points(data)
    assert actual == expected

def test_order_by_points_all_positive():
    data = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    actual = order_by_points(data)
    assert actual == expected