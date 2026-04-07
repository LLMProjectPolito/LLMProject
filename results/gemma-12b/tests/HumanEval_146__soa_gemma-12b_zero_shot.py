
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
    return int(digit) % 2 != 0

def check_first_and_last_digit_odd(num):
    num_str = str(abs(num))
    if not num_str:
        return False
    return is_odd_digit(num_str[0]) and is_odd_digit(num_str[-1])

@pytest.fixture
def sample_data():
    return [
        [15, -73, 14, -15],
        [33, -2, -3, 45, 21, 109],
        [11, 13, 15, 17, 19, 21, 23, 25, 27, 29],
        [22, 24, 26, 28, 30],
        [123, 456, 789, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191],
        [],
        [10, 20, 30, 40, 50],
        [11111, 33333, 55555, 77777, 99999],
        [1, 3, 5, 7, 9],
        [100, 300, 500, 700, 900],
        [-11, -33, -55, -77, -99],
        [11.5, 33.7, 55.9, 77.1, 99.3],
        [15.1, 35.3, 55.5, 75.7, 95.9]
    ]

def test_specialFilter_empty_list(sample_data):
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_elements(sample_data):
    assert specialFilter([10, 20, 30]) == 0

def test_specialFilter_basic_example1(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_basic_example2(sample_data):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_matching(sample_data):
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_mixed_positive_negative(sample_data):
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 4

def test_specialFilter_large_numbers(sample_data):
    assert specialFilter([123, 456, 789, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]) == 10

def test_specialFilter_numbers_with_zeros(sample_data):
    assert specialFilter([100, 300, 500, 700, 900]) == 0

def test_specialFilter_negative_numbers_with_odd_digits(sample_data):
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_specialFilter_floating_point_numbers(sample_data):
    assert specialFilter([11.5, 33.7, 55.9, 77.1, 99.3]) == 0

def test_specialFilter_floating_point_numbers_with_odd_digits(sample_data):
    assert specialFilter([15.1, 35.3, 55.5, 75.7, 95.9]) == 0

def test_specialFilter_single_element_matching(sample_data):
    assert specialFilter([15]) == 1

def test_specialFilter_single_element_not_matching(sample_data):
    assert specialFilter([14]) == 0

def test_specialFilter_large_list(sample_data):
    large_list = list(range(1, 101))
    count = 0
    for num in large_list:
        if num > 10 and check_first_and_last_digit_odd(num):
            count += 1
    assert specialFilter(large_list) == count