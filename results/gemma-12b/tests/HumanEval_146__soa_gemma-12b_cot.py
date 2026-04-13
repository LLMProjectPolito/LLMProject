
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
        [91, 92, 93, 94, 95],
        [15, 16, 17, 18, 19],
        [15, 25, 35, 45, 55],
        [-15, -25, -35, -45, -55],
        [15, -15, 15, -15],
        [15, 15, 15, 15],
        [15, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
        [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
    ]

def test_specialFilter_empty_list(sample_data):
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_elements(sample_data):
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_basic_example1(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_basic_example2(sample_data):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_matching(sample_data):
    assert specialFilter([15, 35, 55, 75, 95]) == 5

def test_specialFilter_mixed_positive_negative(sample_data):
    assert specialFilter([15, -73, 14, -15, 35, -55]) == 2

def test_specialFilter_large_numbers(sample_data):
    assert specialFilter([151, 353, 555, 757, 959]) == 5

def test_specialFilter_numbers_close_to_10(sample_data):
    assert specialFilter([9, 11, 12, 13, 14, 15]) == 1

def test_specialFilter_numbers_greater_than_10(sample_data):
    assert specialFilter([11, 12, 13, 14, 15, 16, 17, 18, 19]) == 1

def test_specialFilter_negative_numbers_with_odd_digits(sample_data):
    assert specialFilter([-15, -35, -55, -75, -95]) == 5

def test_specialFilter_zero_and_positive_numbers(sample_data):
    assert specialFilter([0, 15, 35, 55]) == 3

def test_specialFilter_all_numbers_less_than_10(sample_data):
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_numbers_with_leading_zeros(sample_data):
    assert specialFilter([15, 015, 035]) == 2

def test_specialFilter_numbers_with_trailing_zeros(sample_data):
    assert specialFilter([150, 350, 550]) == 0

def test_specialFilter_numbers_with_both_leading_and_trailing_zeros(sample_data):
    assert specialFilter([0150, 0350, 0550]) == 0

def test_specialFilter_numbers_with_mixed_digits(sample_data):
    assert specialFilter([123, 456, 789, 101]) == 0

def test_specialFilter_numbers_with_special_characters(sample_data):
    assert specialFilter([15, 15.0, 15.5]) == 1

def test_specialFilter_large_list(sample_data):
    large_list = list(range(1, 101))
    assert specialFilter(large_list) == 10