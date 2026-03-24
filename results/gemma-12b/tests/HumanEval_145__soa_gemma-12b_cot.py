
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
def multiple_elements_data():
    return [10, 1, 11, 2, 21]

@pytest.fixture
def negative_numbers_data():
    return [-1, -10, -11, -2, -20]

@pytest.fixture
def mixed_positive_negative_data():
    return [1, -1, 10, -10, 11, -11]

def test_order_by_points_sample_data(sample_data):
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_data) == expected

def test_order_by_points_empty_data(empty_data):
    assert order_by_points(empty_data) == []

def test_order_by_points_single_element_data(single_element_data):
    assert order_by_points(single_element_data) == single_element_data

def test_order_by_points_multiple_elements_data(multiple_elements_data):
    expected = [1, 10, 11, 2, 21]
    assert order_by_points(multiple_elements_data) == expected

def test_order_by_points_negative_numbers_data(negative_numbers_data):
    expected = [-1, -10, -11, -2, -20]
    assert order_by_points(negative_numbers_data) == expected

def test_order_by_points_mixed_positive_negative_data(mixed_positive_negative_data):
    expected = [1, -1, 10, -10, 11, -11]
    assert order_by_points(mixed_positive_negative_data) == expected

def test_order_by_points_with_zeros(mixed_positive_negative_data):
    data = [10, -10, 0, 1, -1]
    expected = [0, 1, -1, 10, -10]
    assert order_by_points(data) == expected

def test_order_by_points_same_digit_sum(data):
    data = [12, 21, 3, 1, 4]
    expected = [3, 1, 4, 12, 21]
    assert order_by_points(data) == expected

def test_order_by_points_large_numbers(data):
    data = [123, 321, 111, 222]
    expected = [111, 222, 123, 321]
    assert order_by_points(data) == expected

def test_order_by_points_all_negative_same_digit_sum(data):
    data = [-12, -21, -3, -1, -4]
    expected = [-3, -1, -4, -12, -21]
    assert order_by_points(data) == expected