
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
from your_module import specialFilter  # Replace your_module

def is_odd_digit(digit):
    return digit in '13579'

def check_first_and_last_digit(num):
    """Checks if the first and last digits of a number are odd."""
    num_str = str(abs(num))  # Handle negative numbers
    if not num_str:
        return False
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return is_odd_digit(first_digit) and is_odd_digit(last_digit)

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([11, 33, 55, 77, 99], 5),
        ([12, 23, 34, 45, 56, 67, 78, 89, 90], 0),
        ([111, 333, 555, 777, 999], 5),
        ([1, 3, 5, 7, 9], 0),
        ([10, 11, 12, 13, 14, 15], 1),
        ([20, 21, 22, 23, 24, 25], 1),
        ([], 0),
        ([15, 15, 15, 15], 4),
        ([15, 15, 15, 15, 10], 4),
        ([-15, -33, -55, -77, -99], 5),
        ([15.0, 33.0, 55.0, 77.0, 99.0], 5),
        ([15.1, 33.3, 55.5, 77.7, 99.9], 5),
        ([15, 33, 55, 77, 99, 10], 5),
        ([15, 33, 55, 77, 99, 11], 6),
        ([15, 33, 55, 77, 99, 101], 6),
        ([15, 33, 55, 77, 99, 100], 5),
        ([15, 33, 55, 77, 99, 1001], 6),
        ([15, 33, 55, 77, 99, 1000], 5)
    ]

def test_specialFilter_positive_cases(sample_data):
    """Tests with positive cases."""
    for nums, expected in sample_data:
        assert specialFilter(nums) == expected

def test_specialFilter_empty_list(sample_data):
    """Tests with an empty list."""
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers(sample_data):
    """Tests with a list containing no matching numbers."""
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_negative_numbers_only(sample_data):
    """Tests with a list containing only negative numbers."""
    assert specialFilter([-1, -2, -3, -4, -5]) == 1

def test_specialFilter_mixed_positive_and_negative(sample_data):
    """Tests with a list containing mixed positive and negative numbers."""
    assert specialFilter([-15, 15, -33, 33]) == 4

def test_specialFilter_large_numbers(sample_data):
    """Tests with large numbers."""
    assert specialFilter([12345, 67890, 98765]) == 1

def test_specialFilter_numbers_with_zeros(sample_data):
    """Tests with numbers containing zeros."""
    assert specialFilter([101, 303, 505, 707, 909]) == 5

def test_specialFilter_numbers_with_leading_zeros(sample_data):
    """Tests with numbers that might have leading zeros (though not strictly valid)."""
    assert specialFilter([015, 033, 055, 077, 099]) == 5

def test_specialFilter_float_numbers(sample_data):
    """Tests with float numbers."""
    assert specialFilter([15.0, 33.0, 55.0, 77.0, 99.0]) == 5

def test_specialFilter_edge_cases(sample_data):
    """Tests with edge cases."""
    assert specialFilter([11, 13, 15, 17, 19]) == 0
    assert specialFilter([31, 33, 35, 37, 39]) == 0
    assert specialFilter([51, 53, 55, 57, 59]) == 0
    assert specialFilter([71, 73, 75, 77, 79]) == 0
    assert specialFilter([91, 93, 95, 97, 99]) == 0