
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
        [15, 17, 19, 21, 23],
        [15, 17, 19, 21, 23, -15, -17, -19],
        [15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909],
        [15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909, 1111, 3333, 5555, 7777, 9999],
        [15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909, 1111, 3333, 5555, 7777, 9999, 10, 20, 30],
        [15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909, 1111, 3333, 5555, 7777, 9999, 10, 20, 30, 11, 12, 13, 14, 15],
    ]

def test_specialFilter_empty_list(sample_data):
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers(sample_data):
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_basic_case(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple_matching_numbers(sample_data):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_matching_numbers(sample_data):
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_mixed_numbers(sample_data):
    assert specialFilter([11, 12, 13, 14, 15]) == 1

def test_specialFilter_negative_numbers(sample_data):
    assert specialFilter([15, 17, 19, 21, 23, -15, -17, -19]) == 8

def test_specialFilter_large_numbers(sample_data):
    assert specialFilter([15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909]) == 13

def test_specialFilter_very_large_numbers(sample_data):
    assert specialFilter([15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909, 1111, 3333, 5555, 7777, 9999]) == 18

def test_specialFilter_with_zeros(sample_data):
    assert specialFilter([15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909, 1111, 3333, 5555, 7777, 9999, 10, 20, 30]) == 20

def test_specialFilter_complex_case(sample_data):
    assert specialFilter([15, 17, 19, 21, 23, -15, -17, -19, 101, 303, 505, 707, 909, 1111, 3333, 5555, 7777, 9999, 10, 20, 30, 11, 12, 13, 14, 15]) == 25