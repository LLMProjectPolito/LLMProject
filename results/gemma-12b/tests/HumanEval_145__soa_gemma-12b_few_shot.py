
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
def negative_and_positive_data():
    return [-5, 5, -10, 10, -15, 15]

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

def test_order_by_points_negative_and_positive_data(negative_and_positive_data):
    expected = [-5, 5, -10, 10, -15, 15]
    assert order_by_points(negative_and_positive_data) == expected

def test_order_by_points_with_zeros():
    data = [0, 10, -10, 100, -100]
    expected = [0, -10, 10, -100, 100]
    assert order_by_points(data) == expected

def test_order_by_points_same_digit_sum():
    data = [1, 10, 100]
    expected = [1, 10, 100]
    assert order_by_points(data) == expected

def test_order_by_points_large_numbers():
    data = [123, 45, 678, 9]
    expected = [9, 45, 123, 678]
    assert order_by_points(data) == expected

def test_order_by_points_mixed_positive_negative_same_sum():
    data = [1, -1, 10, -10]
    expected = [1, -1, 10, -10]
    assert order_by_points(data) == expected

def test_order_by_points_all_negative():
    data = [-1, -2, -3, -4]
    expected = [-1, -2, -3, -4]
    assert order_by_points(data) == expected