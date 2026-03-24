
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

def test_no_special_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_single_special_number():
    assert specialFilter([15]) == 1
    assert specialFilter([11]) == 1
    assert specialFilter([33]) == 1
    assert specialFilter([55]) == 1
    assert specialFilter([77]) == 1
    assert specialFilter([99]) == 1

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 55, 77, 99]) == 5
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    assert specialFilter([-15, -33, -55]) == 3
    assert specialFilter([-12, -34, -56]) == 0
    assert specialFilter([-11, -13, -15]) == 3

def test_mixed_numbers():
    assert specialFilter([15, -33, 45, -77, 10, 22]) == 3
    assert specialFilter([12, -35, 46, -79, 11, 23]) == 2

def test_large_numbers():
    assert specialFilter([100001, 100003, 100005]) == 3
    assert specialFilter([100002, 100004, 100006]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0

def test_edge_case_single_digit_odd():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_with_leading_zeros():
    assert specialFilter([015]) == 0 # Should treat as 15
    assert specialFilter([033]) == 0 # Should treat as 33