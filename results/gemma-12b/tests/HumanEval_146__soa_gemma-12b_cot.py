
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
    num_str = str(abs(num))
    if not num_str:
        return False
    first_digit = num_str[0]
    last_digit = num_str[-1]
    return is_odd_digit(first_digit) and is_odd_digit(last_digit)

@pytest.fixture
def sample_data():
    return [
        [15, -73, 14, -15],
        [33, -2, -3, 45, 21, 109],
        [11, 22, 33, 44, 55, 66, 77, 88, 99],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [111, 222, 333, 444, 555, 666, 777, 888, 999],
        [],
        [10, 20, 30, 40, 50],
        [11, 12, 13, 14, 15],
        [99, 98, 97, 96, 95],
        [15, 16, 17, 18, 19],
        [15, -73, 14, -15, 21, 33, 45, 57, 69, 71, 83, 95],
        [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    ]

def test_specialFilter_empty_list(sample_data):
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_elements(sample_data):
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_basic_case(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple_matching_elements(sample_data):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_matching_elements(sample_data):
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_mixed_positive_negative(sample_data):
    assert specialFilter([15, -73, 14, -15, 21, 33, 45, 57, 69, 71, 83, 95]) == 8

def test_specialFilter_large_list(sample_data):
    data = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    assert specialFilter(data) == 48

def test_specialFilter_numbers_greater_than_10(sample_data):
    assert specialFilter([11, 12, 13, 14, 15]) == 3

def test_specialFilter_numbers_less_than_10(sample_data):
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_negative_numbers(sample_data):
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_specialFilter_zero(sample_data):
    assert specialFilter([0]) == 0

def test_specialFilter_with_zero_and_valid_numbers(sample_data):
    assert specialFilter([0, 15, -73]) == 1

def test_specialFilter_with_large_numbers(sample_data):
    assert specialFilter([1500, -7300, 1400, -1500]) == 1

def test_specialFilter_with_decimal_numbers(sample_data):
    assert specialFilter([15.5, -73.3, 14.1, -15.7]) == 0

def test_specialFilter_with_special_characters(sample_data):
    assert specialFilter([15, -73, "abc", 14, -15]) == 1