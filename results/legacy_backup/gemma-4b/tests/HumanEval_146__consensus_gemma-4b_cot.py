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
    assert specialFilter([15, 25, 35, 45, 55]) == 5

def test_specialFilter_mixed_numbers():
    assert specialFilter([15, -73, 14, -15, 21, 109]) == 2

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -25, -35]) == 0

def test_specialFilter_numbers_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def test_specialFilter_with_zero():
    assert specialFilter([11, 22, 33, 44, 55]) == 0

def test_specialFilter_with_negative_and_positive():
    assert specialFilter([-15, 25, -35, 45]) == 2

def test_specialFilter_large_numbers():
    assert specialFilter([111115, 222225, 333335]) == 3

def test_specialFilter_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 3

def test_specialFilter_edge_case_single_digit():
    assert specialFilter([11, 33, 55, 77, 99]) == 0

def test_specialFilter_edge_case_two_digits():
    assert specialFilter([11, 33, 55, 77, 99]) == 0

def test_specialFilter_with_zero_in_number():
    assert specialFilter([101, 202, 303]) == 0

def test_specialFilter_with_negative_zero():
    assert specialFilter([-101, -202, -303]) == 0