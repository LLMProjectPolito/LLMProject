
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

@pytest.fixture
def list_with_negative_numbers():
    return [-5, -10, -1, 1, 10, 5]

@pytest.fixture
def list_with_same_digit_sum():
    return [1, 10, 100, 1000]

@pytest.fixture
def list_with_non_integer():
    return [1, "11", 2.5, -1]

@pytest.fixture
def list_with_mixed_types():
    return [1, "11", 2.5, -1, 11]

def test_order_by_points_sample(sample_list):
    assert order_by_points(sample_list) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty(empty_list):
    assert order_by_points(empty_list) == []

def test_order_by_points_single_element(single_element_list):
    assert order_by_points(single_element_list) == single_element_list

def test_order_by_points_with_zeros(list_with_zeros):
    assert order_by_points(list_with_zeros) == [0, -10, 10, 100]

def test_order_by_points_with_negative_numbers(list_with_negative_numbers):
    assert order_by_points(list_with_negative_numbers) == [-1, -10, -5, 1, 5, 10]

def test_order_by_points_with_same_digit_sum(list_with_same_digit_sum):
    # This test assumes the current implementation preserves original order
    # for elements with the same digit sum. If the sorting algorithm is
    # changed to be stable, this test might need adjustment.
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

def test_order_by_points_with_zero_input():
    assert order_by_points([0]) == [0]

def test_order_by_points_single_negative_number():
    assert order_by_points([-5]) == [-5]

def test_order_by_points_large_number_edge_case():
    assert order_by_points([999999999]) == [999999999]

def test_order_by_points_none_input():
    assert order_by_points(None) == []

def test_order_by_points_non_integer_input(list_with_non_integer):
    # Assuming the function ignores non-integer values
    assert order_by_points(list_with_non_integer) == [1, -1, 2.5, 11]

def test_order_by_points_empty_string_input():
    assert order_by_points("") == []

def test_order_by_points_mixed_data_types(list_with_mixed_types):
    # Assuming the function ignores non-integer values
    assert order_by_points(list_with_mixed_types) == [1, -1, 2.5, 11]