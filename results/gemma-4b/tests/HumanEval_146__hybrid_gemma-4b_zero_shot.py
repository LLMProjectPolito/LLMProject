
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
                if (first_digit % 2 != 0 and last_digit % 2 != 0):
                    count += 1
    return count

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_single_matching_number():
    assert specialFilter([15]) == 1

def test_specialFilter_multiple_matching_numbers():
    assert specialFilter([15, 33, 45, 109]) == 3

def test_specialFilter_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([-15, 33, -45, 109]) == 2

def test_specialFilter_with_zero():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_with_large_numbers():
    assert specialFilter([111, 133, 155, 177, 199]) == 5

def test_specialFilter_with_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 1

def test_specialFilter_with_negative_and_positive():
    assert specialFilter([-15, 15, -33, 33]) == 2

def test_specialFilter_with_edge_cases():
    assert specialFilter([11, 12, 13, 14, 15]) == 1
    assert specialFilter([101, 123, 131, 145, 151]) == 3
    assert specialFilter([-101, -123, -131, -145, -151]) == 0
    assert specialFilter([1111, 1333, 1555, 1777, 1999]) == 5
    assert specialFilter([-1111, -1333, -1555, -1777, -1999]) == 0
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 1
    assert specialFilter([-11, -13, -15, -17, -19, -21, -23, -25, -27, -29]) == 0
    assert specialFilter([11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 8
    assert specialFilter([-11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -31, -33, -35, -37, -39]) == 0

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_matching_numbers():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_single_matching_number():
    assert specialFilter([15]) == 1

def test_multiple_matching_numbers():
    assert specialFilter([15, 33, 45, 109]) == 3

def test_negative_numbers():
    assert specialFilter([-15, -33, -45]) == 0

def test_mixed_positive_negative():
    assert specialFilter([-15, 33, -45, 109]) == 2

def test_numbers_less_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_numbers_greater_than_10_no_odd_digits():
    assert specialFilter([12, 14, 16, 18]) == 0

def test_numbers_greater_than_10_one_odd_digit():
    assert specialFilter([11, 33, 55, 77, 99]) == 0

def test_numbers_greater_than_10_both_odd_digits():
    assert specialFilter([111, 333, 555, 777, 999]) == 0

def test_large_numbers():
    assert specialFilter([1111111115, 3333333333]) == 2

def test_zero_as_first_digit():
    assert specialFilter([101, 103, 105, 107, 109]) == 0

def test_zero_as_last_digit():
    assert specialFilter([110, 330, 550, 770, 990]) == 0

def test_mixed_zero_and_odd_digits():
    assert specialFilter([101, 103, 105, 107, 109, 100]) == 1

def test_duplicate_numbers():
    assert specialFilter([15, 15, 15]) == 1

def test_negative_and_positive_mixed():
    assert specialFilter([-15, 15, -33, 33]) == 2

def test_edge_cases():
    assert specialFilter([11, 13, 15, 17, 19]) == 0
    assert specialFilter([11, 13, 15, 17, 19, 21]) == 0
    assert specialFilter([11, 13, 15, 17, 19, 23]) == 1