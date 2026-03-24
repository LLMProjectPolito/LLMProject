
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
        ([100, 200, 300, 400, 500], 0),
        ([101, 111, 121, 131, 141], 1),
        ([-11, -33, -55, -77, -99], 0),
        ([15, 16, 17, 18, 19], 1),
        ([35, 36, 37, 38, 39], 1),
        ([55, 56, 57, 58, 59], 1),
        ([75, 76, 77, 78, 79], 1),
        ([95, 96, 97, 98, 99], 1),
        ([11, 12, 13, 14, 15, 16, 17, 18, 19, 21], 2),
        ([101, 102, 103, 104, 105, 106, 107, 108, 109, 201], 2),
        ([15, 25, 35, 45, 55, 65, 75, 85, 95], 0),
    ]

def test_special_filter_valid_cases(sample_data):
    """Tests the function with valid input cases."""
    for nums, expected in sample_data:
        assert specialFilter(nums) == expected

def test_special_filter_empty_list(sample_data):
    """Tests the function with an empty list."""
    assert specialFilter([]) == 0

def test_special_filter_no_matching_numbers(sample_data):
    """Tests the function when no numbers match the criteria."""
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_special_filter_negative_numbers(sample_data):
    """Tests the function with negative numbers."""
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_special_filter_mixed_positive_and_negative(sample_data):
    """Tests the function with a mix of positive and negative numbers."""
    assert specialFilter([-15, 15, -33, 33]) == 2

def test_special_filter_large_numbers(sample_data):
    """Tests the function with large numbers."""
    assert specialFilter([12345, 67890, 98765]) == 1

def test_special_filter_single_digit_numbers(sample_data):
    """Tests the function with single-digit numbers."""
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_special_filter_zero(sample_data):
    """Tests the function with zero."""
    assert specialFilter([0]) == 0

def test_special_filter_numbers_equal_to_10(sample_data):
    """Tests the function with numbers equal to 10."""
    assert specialFilter([10]) == 0

def test_special_filter_numbers_greater_than_10(sample_data):
    """Tests the function with numbers greater than 10."""
    assert specialFilter([11, 12, 13]) == 1