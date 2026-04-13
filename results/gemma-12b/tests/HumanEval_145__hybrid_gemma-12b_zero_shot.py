
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
def sample_data():
    """Fixture providing sample data for testing."""
    return [1, 11, -1, -11, -12]

@pytest.fixture
def empty_data():
    """Fixture providing empty data for testing."""
    return []

@pytest.fixture
def single_element_data():
    """Fixture providing single element data for testing."""
    return [5]

@pytest.fixture
def duplicate_sums_data():
    """Fixture providing data with duplicate sums for testing."""
    return [1, 10, 11, 2, 20]

@pytest.fixture
def negative_numbers_data():
    """Fixture providing data with negative numbers for testing."""
    return [-1, -10, -11, -2, -20]

@pytest.fixture
def mixed_positive_negative_data():
    """Fixture providing data with mixed positive and negative numbers."""
    return [1, -1, 10, -10, 11, -11]

@pytest.fixture
def large_numbers_data():
    """Fixture providing large numbers for testing."""
    return [12345, 6789, 1000, 1]

@pytest.fixture
def zeroes_data():
    """Fixture providing zeroes for testing."""
    return [0, 10, 0, 20]

@pytest.fixture
def same_digit_sum_data():
    """Fixture providing data with the same digit sum."""
    return [1, 10, 100, 1000]

@pytest.fixture
def with_duplicates():
    """Fixture providing data with duplicate numbers."""
    return [1, 1, 2, 2]


def test_order_by_points_sample_data(sample_data):
    """Test with the sample data provided in the problem description."""
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_data) == expected

def test_order_by_points_empty_data(empty_data):
    """Test with empty data."""
    assert order_by_points(empty_data) == []

def test_order_by_points_single_element_data(single_element_data):
    """Test with a single element."""
    assert order_by_points(single_element_data) == single_element_data

def test_order_by_points_duplicate_sums_data(duplicate_sums_data):
    """Test with data containing duplicate sums, ensuring original index is preserved."""
    expected = [1, 2, 10, 11, 20]
    assert order_by_points(duplicate_sums_data) == expected

def test_order_by_points_negative_numbers_data(negative_numbers_data):
    """Test with only negative numbers."""
    expected = [-1, -2, -10, -11, -20]
    assert order_by_points(negative_numbers_data) == expected

def test_order_by_points_mixed_positive_negative_data(mixed_positive_negative_data):
    """Test with a mix of positive and negative numbers."""
    expected = [1, -1, 10, -10, 11, -11]
    assert order_by_points(mixed_positive_negative_data) == expected

def test_order_by_points_large_numbers(large_numbers_data):
    """Test with large numbers to ensure digit sum calculation is correct."""
    expected = [1, 1000, 12345, 6789]
    assert order_by_points(large_numbers_data) == expected

def test_order_by_points_zeroes(zeroes_data):
    """Test with zeroes."""
    expected = [0, 0, 10, 20]
    assert order_by_points(zeroes_data) == expected

def test_order_by_points_all_same_digit_sum(same_digit_sum_data):
    """Test with all numbers having the same digit sum."""
    expected = [1, 10, 100, 1000]
    assert order_by_points(same_digit_sum_data) == expected

def test_order_by_points_with_duplicates(with_duplicates):
    """Test with duplicate numbers in the input list."""
    expected = [1, 1, 2, 2]
    assert order_by_points(with_duplicates) == expected