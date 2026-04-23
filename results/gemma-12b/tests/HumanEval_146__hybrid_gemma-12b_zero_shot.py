
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
        ([22, 44, 66, 88], 0),
        ([12, 34, 56, 78, 90], 0),
        ([1, 3, 5, 7, 9], 0),
        ([111, 333, 555, 777, 999], 5),
        ([101, 303, 505, 707, 909], 5),
        ([110, 330, 550, 770, 990], 0),
        ([150, 350, 550, 750, 950], 0),
        ([15, 73, 14, 15], 2),
        ([], 0),
        ([11, 12, 13, 14, 15], 1),
        ([31, 32, 33, 34, 35], 1),
        ([51, 52, 53, 54, 55], 1),
        ([71, 72, 73, 74, 75], 1),
        ([91, 92, 93, 94, 95], 1),
        ([100, 200, 300, 400, 500], 0),
        ([101, 202, 303, 404, 505], 1),
        ([-11, -33, -55, -77, -99], 5),
        ([-15, -73, -14, -15], 1),
        ([15.0, 73.0, 14.0, 15.0], 1), # Test with floats
        ([15.1, 73.2, 14.3, 15.4], 0) # Test with floats
    ]

@pytest.mark.parametrize("nums, expected", sample_data)
def test_specialFilter(nums, expected):
    """Tests the specialFilter function with various inputs."""
    assert specialFilter(nums) == expected

def test_empty_list():
    """Tests with an empty list."""
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    """Tests with a list containing no matching numbers."""
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_all_matching_numbers():
    """Tests with a list containing all matching numbers."""
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_negative_numbers():
    """Tests with negative numbers."""
    assert specialFilter([-11, -33, -55, -77, -99]) == 5

def test_mixed_positive_and_negative():
    """Tests with a mix of positive and negative numbers."""
    assert specialFilter([-11, 13, -33, 55, -77, 99]) == 4

def test_large_numbers():
    """Tests with large numbers."""
    assert specialFilter([11111, 33333, 55555, 77777, 99999]) == 5

def test_zero():
    """Tests with zero."""
    assert specialFilter([0]) == 0

def test_single_element_list():
    """Tests with a single element list."""
    assert specialFilter([15]) == 1
    assert specialFilter([14]) == 0
    assert specialFilter([33]) == 1
    assert specialFilter([22]) == 0