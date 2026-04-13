
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
        if num > 10 and (str(num)[0] in '13579' and str(num)[-1] in '13579'):
            count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_elements():
    assert specialFilter([-1, -2, -3]) == 0

def test_single_matching_element():
    assert specialFilter([15]) == 1

def test_single_non_matching_element():
    assert specialFilter([14]) == 0

def test_multiple_matching_elements():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_multiple_non_matching_elements():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -35, -75]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([-15, 15, -35, 35]) == 2

def test_large_numbers():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_numbers_with_zero():
    assert specialFilter([101, 103, 105, 107, 109]) == 0

def test_numbers_with_odd_first_digit_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_even_first_digit_odd_last_digit():
    assert specialFilter([21, 43, 65, 87, 109]) == 0

def test_numbers_with_both_digits_even():
    assert specialFilter([22, 44, 66, 88, 100]) == 0

def test_edge_case_1():
    assert specialFilter([1111, 3333, 5555, 7777, 9999]) == 5

def test_edge_case_2():
    assert specialFilter([11, 33, 55, 77, 99]) == 0

def test_edge_case_3():
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_mixed_edge_case():
    assert specialFilter([111, 333, 555, 777, 999, 11, 33, 55, 77, 99]) == 5