
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
        [11, 22, 33, 44, 55],
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10],
        [123, 321, 543, 789],
        [10, 20, 30, 40, 50],
        [111, 222, 333, 444, 555],
        [101, 202, 303, 404, 505],
        [],
        [15, 15, 15, 15],
        [-15, -15, -15, -15],
        [15, -15, 15, -15],
        [15.0, -15.0],
        [15.5, -15.5],
        [151, -151, 153, -153],
        [1011, 1101, 1013, 1301],
        [100, 200, 300, 400, 500],
        [1001, 2002, 3003, 4004, 5005],
        [1000, 2000, 3000, 4000, 5000]
    ]

def test_specialFilter_empty_list(sample_data):
    assert specialFilter([]) == 0

def test_specialFilter_no_matches(sample_data):
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_single_match(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple_matches(sample_data):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_all_matches(sample_data):
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_mixed_positive_negative(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_large_numbers(sample_data):
    assert specialFilter([123, 321, 543, 789]) == 4

def test_specialFilter_numbers_with_zeros(sample_data):
    assert specialFilter([101, 202, 303, 404, 505]) == 5

def test_specialFilter_numbers_with_leading_zeros(sample_data):
    assert specialFilter([1001, 2002, 3003, 4004, 5005]) == 5

def test_specialFilter_decimal_numbers(sample_data):
    assert specialFilter([15.0, -15.0]) == 0
    assert specialFilter([15.5, -15.5]) == 0

def test_specialFilter_negative_numbers_with_odd_digits(sample_data):
    assert specialFilter([-15, -15, -15, -15]) == 4

def test_specialFilter_edge_case_1(sample_data):
    assert specialFilter([151, -151, 153, -153]) == 4

def test_specialFilter_edge_case_2(sample_data):
    assert specialFilter([1011, 1101, 1013, 1301]) == 0

def test_specialFilter_numbers_ending_in_zero(sample_data):
    assert specialFilter([100, 200, 300, 400, 500]) == 0

def test_specialFilter_large_numbers_ending_in_zero(sample_data):
    assert specialFilter([1000, 2000, 3000, 4000, 5000]) == 0