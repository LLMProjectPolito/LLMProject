
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

def test_multiple_special_numbers():
    assert specialFilter([15, 33, 55, 77, 99]) == 5

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_large_numbers():
    assert specialFilter([101, 123, 157, 189, 1001]) == 4

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_complex_case():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_zero_in_number():
    assert specialFilter([101, 103, 105, 107, 109]) == 0

def test_all_negative_numbers():
    assert specialFilter([-11, -13, -15, -22, -23]) == 3

def test_mixed_positive_and_negative():
    assert specialFilter([11, -13, 15, -17, 19, -21]) == 4

def test_single_digit_special_number():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_two_digit_special_number():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_large_special_number():
    assert specialFilter([1111111111]) == 1

def test_mixed_large_and_small():
    assert specialFilter([15, 1001, 37, 12, 59]) == 2

def test_all_negative():
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_negative_and_positive():
    assert specialFilter([-15, 15, -37, 37]) == 2

def test_numbers_with_even_first_digit():
    assert specialFilter([21, 43, 65, 87, 09]) == 0

def test_numbers_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_both_even_digits():
    assert specialFilter([24, 46, 68, 80]) == 0

def test_numbers_greater_than_10_but_not_special():
    assert specialFilter([12, 14, 16, 18, 21]) == 0

def test_numbers_less_than_or_equal_to_10():
    assert specialFilter([1, 3, 5, 7, 9, 10]) == 0

def test_large_numbers():
    assert specialFilter([1001, 1003, 1005, 1007, 1009]) == 0