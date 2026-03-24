
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

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_matching_number():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matching_numbers():
    assert specialFilter([15, 22, 33, 44, 55]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -22, -33, -44, -55]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([-15, 22, -33, 44, -55]) == 0

def test_specialFilter_with_zero():
    assert specialFilter([11, 22, 33, 44, 55]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([111, 222, 333, 444, 555]) == 0

def test_specialFilter_example_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_example_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_edge_case_single_digit_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 0

def test_specialFilter_edge_case_single_digit_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_edge_case_first_digit_odd_last_digit_even():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_specialFilter_edge_case_first_digit_even_last_digit_odd():
    assert specialFilter([21, 43, 65, 87, 109]) == 0

def test_specialFilter_edge_case_first_digit_even_last_digit_even():
    assert specialFilter([22, 44, 66, 88, 100]) == 0

def test_specialFilter_edge_case_first_digit_odd_last_digit_zero():
    assert specialFilter([10, 30, 50, 70, 90]) == 0

def test_specialFilter_edge_case_negative_first_digit_odd_negative_last_digit_odd():
    assert specialFilter([-15, -33, -55]) == 0

def test_specialFilter_edge_case_negative_first_digit_odd_negative_last_digit_even():
    assert specialFilter([-12, -34, -56]) == 0

def test_specialFilter_edge_case_negative_first_digit_even_negative_last_digit_odd():
    assert specialFilter([-21, -43, -65]) == 0