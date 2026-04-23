
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
    return [-1, -2, -3, -4, -5]

@pytest.fixture
def list_with_large_numbers():
    return [12345, 67890, 11111, 22222]

@pytest.fixture
def list_with_mixed_signs():
    return [1, -1, 10, -10, 100, -100]

@pytest.fixture
def list_with_duplicate_numbers():
    return [1, 2, 1, 2, 3]

@pytest.fixture
def list_with_leading_zeros():
    return ["001", "010", "100"]

@pytest.fixture
def list_with_non_numeric():
    return [1, "a", 2]

@pytest.fixture
def list_with_large_number():
    return [9999999999, 10000000000]

def test_order_by_points_sample(sample_list):
    assert order_by_points(sample_list) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty(empty_list):
    assert order_by_points(empty_list) == []

def test_order_by_points_single_element(single_element_list):
    assert order_by_points(single_element_list) == single_element_list

def test_order_by_points_zeros_present(list_with_zeros):
    assert order_by_points(list_with_zeros) == [0, -10, 10, 100]

def test_order_by_points_negative_numbers(list_with_negative_numbers):
    assert order_by_points(list_with_negative_numbers) == [-1, -2, -3, -4, -5]

def test_order_by_points_large_numbers(list_with_large_numbers):
    assert order_by_points(list_with_large_numbers) == [11111, 22222, 12345, 67890]

def test_order_by_points_mixed_signs(list_with_mixed_signs):
    assert order_by_points(list_with_mixed_signs) == [1, -1, 10, -10, 100, -100]

def test_order_by_points_same_digit_sum(list_with_duplicate_numbers):
    assert order_by_points(list_with_duplicate_numbers) == [1, 2, 1, 2, 3]

def test_order_by_points_all_same_digit_sum():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_negative_and_positive_same_sum():
    assert order_by_points([1, -1]) == [1, -1]

def test_order_by_points_zero_and_positive():
    assert order_by_points([0, 1]) == [0, 1]

def test_order_by_points_zero_and_negative():
    assert order_by_points([0, -1]) == [0, -1]

def test_order_by_points_large_numbers_same_digit_sum(list_with_large_number):
    assert order_by_points(list_with_large_number) == [9999999999, 10000000000]

def test_order_by_points_leading_zeros():
    assert order_by_points(list_with_leading_zeros) == ['001', '010', '100']

def test_order_by_points_non_integer_input(list_with_non_numeric):
    with pytest.raises(TypeError):
        order_by_points(list_with_non_numeric)

def test_order_by_points_negative_zero():
    assert order_by_points([-0, 0, 1]) == [0, -0, 1]

def test_order_by_points_tie_breaking():
    assert order_by_points([1, 10, 100]) == [1, 10, 100]