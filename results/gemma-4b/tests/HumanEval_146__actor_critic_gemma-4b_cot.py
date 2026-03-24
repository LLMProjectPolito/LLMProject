
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_elements():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_element():
    assert specialFilter([15]) == 1

def test_multiple_matching_elements():
    assert specialFilter([15, 25, 35, 45, 55]) == 5

def test_mixed_elements():
    assert specialFilter([15, -73, 14, -15, 25, 33]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -25, -35]) == 0

def test_large_numbers():
    assert specialFilter([115, 125, 135]) == 3

def test_edge_case_single_digit_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 0

def test_edge_case_single_digit_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_edge_case_first_digit_odd_last_digit_even():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_edge_case_first_digit_even_last_digit_odd():
    assert specialFilter([21, 43, 65, 87, 109]) == 0

def test_edge_case_first_digit_last_digit_odd():
    assert specialFilter([15, 35, 55, 75, 95]) == 5

def test_edge_case_first_digit_last_digit_even():
    assert specialFilter([12, 32, 52, 72, 92]) == 0

def test_mixed_positive_negative_numbers():
    assert specialFilter([-15, 25, -35, 45]) == 2

def test_zero_in_list():
    assert specialFilter([0, 15, 25]) == 1

def test_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 3

def test_complex_case():
    assert specialFilter([115, -23, 335, -45, 555, 775, -89, 995]) == 4