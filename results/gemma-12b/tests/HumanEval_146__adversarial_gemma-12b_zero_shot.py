
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
        [12, 34, 56, 78, 90],
        [10, 20, 30, 40, 50],
        [111, 222, 333, 444, 555],
        [101, 202, 303, 404, 505],
        [11, 13, 15, 17, 19],
        [31, 33, 35, 37, 39],
        [51, 53, 55, 57, 59],
        [71, 73, 75, 77, 79],
        [91, 93, 95, 97, 99],
        [],
        [10],
        [11],
        [101],
        [111],
        [15, 15, 15],
        [-15, -15, -15],
        [15, -15, 15],
        [101, 103, 105, 107, 109],
        [111, 113, 115, 117, 119],
        [151, 153, 155, 157, 159],
        [171, 173, 175, 177, 179],
        [191, 193, 195, 197, 199],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [101, 102, 103, 104, 105],
        [106, 107, 108, 109, 110],
    ]

def test_specialFilter_empty_list(sample_data):
    assert specialFilter([]) == 0

def test_specialFilter_no_matches(sample_data):
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_all_matches(sample_data):
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_mixed_list(sample_data):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_example_2(sample_data):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_single_element_greater_than_10_and_odd_digits(sample_data):
    assert specialFilter([111]) == 1

def test_specialFilter_single_element_less_than_10(sample_data):
    assert specialFilter([11]) == 0

def test_specialFilter_single_element_greater_than_10_but_not_odd_digits(sample_data):
    assert specialFilter([101]) == 0

def test_specialFilter_negative_numbers(sample_data):
    assert specialFilter([-15, -15, -15]) == 0

def test_specialFilter_mixed_positive_and_negative(sample_data):
    assert specialFilter([15, -15, 15]) == 0

def test_specialFilter_large_numbers(sample_data):
    assert specialFilter([101, 103, 105, 107, 109]) == 5

def test_specialFilter_numbers_with_leading_zeros(sample_data):
    assert specialFilter([011, 013, 015]) == 0

def test_specialFilter_numbers_with_multiple_odd_digits(sample_data):
    assert specialFilter([111, 113, 115, 117, 119]) == 5

def test_specialFilter_numbers_with_odd_and_even_digits(sample_data):
    assert specialFilter([11, 12, 13, 14, 15]) == 0

def test_specialFilter_numbers_with_large_values(sample_data):
    assert specialFilter([1111111111, 3333333333, 5555555555]) == 0

def test_specialFilter_edge_case_1(sample_data):
    assert specialFilter([101, 102, 103, 104, 105]) == 0

def test_specialFilter_edge_case_2(sample_data):
    assert specialFilter([106, 107, 108, 109, 110]) == 0