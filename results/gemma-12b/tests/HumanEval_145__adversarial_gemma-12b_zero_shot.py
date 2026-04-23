
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
def multiple_same_digit_sum():
    return [10, 1, 100, 1000]

@pytest.fixture
def negative_numbers():
    return [-1, -2, -3, -4, -5]

@pytest.fixture
def mixed_positive_negative():
    return [1, -1, 2, -2, 3, -3]

def test_order_by_points_sample(sample_data):
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_data) == expected

def test_order_by_points_empty(empty_data):
    assert order_by_points(empty_data) == []

def test_order_by_points_single_element(single_element_data):
    assert order_by_points(single_element_data) == single_element_data

def test_order_by_points_multiple_same_digit_sum(multiple_same_digit_sum):
    expected = [1, 10, 100, 1000]
    assert order_by_points(multiple_same_digit_sum) == expected

def test_order_by_points_negative_numbers(negative_numbers):
    expected = [-1, -2, -3, -4, -5]
    assert order_by_points(negative_numbers) == expected

def test_order_by_points_mixed_positive_negative(mixed_positive_negative):
    expected = [1, -1, 2, -2, 3, -3]
    assert order_by_points(mixed_positive_negative) == expected

def test_order_by_points_zero():
    assert order_by_points([0, 1, -1]) == [0, -1, 1]

def test_order_by_points_large_numbers():
    data = [12345, 6789, 10, 1]
    expected = [1, 10, 12345, 6789]
    assert order_by_points(data) == expected

def test_order_by_points_duplicate_numbers():
    data = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    assert order_by_points(data) == expected

def test_order_by_points_all_negative():
    data = [-1, -2, -3]
    expected = [-1, -2, -3]
    assert order_by_points(data) == expected