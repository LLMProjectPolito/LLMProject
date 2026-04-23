
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).

    Negative numbers are handled by considering their absolute value.
    Non-integer inputs are skipped.
    Leading zeros are not considered part of the number (e.g., '015' is treated as '15').

    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if isinstance(num, int):
            if num > 10:
                num_str = str(abs(num))  # Convert to string and handle negative numbers
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
        # else: skip non-integer inputs
    return count

import pytest

def test_specialFilter_basic1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_basic2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_specialFilter_mixed_numbers():
    assert specialFilter([11, -13, 15, -17, 19, 22, -23]) == 4

def test_specialFilter_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_large_numbers():
    assert specialFilter([121, 133, 155, 177, 199, 202]) == 5

def test_specialFilter_numbers_with_leading_zeros():
    assert specialFilter([101, 103, 105]) == 0  # Leading zeros are not considered

def test_specialFilter_numbers_close_to_10():
    assert specialFilter([11, 12, 13]) == 2

def test_specialFilter_numbers_with_zero_in_between():
    assert specialFilter([101, 103, 105]) == 0

def test_specialFilter_single_digit_greater_than_10():
    assert specialFilter([11]) == 1

def test_specialFilter_numbers_ending_in_zero():
    assert specialFilter([110, 130, 150]) == 0

def test_specialFilter_large_numbers_with_even_digits():
    assert specialFilter([1234567890, 24680]) == 0

def test_specialFilter_mixed_positive_and_negative_large_numbers():
    assert specialFilter([1234567891, -135791, 24680, -11]) == 2

def test_specialFilter_non_integer_input():
    assert specialFilter([15, "abc", 21, True, 3.14]) == 2

def test_specialFilter_very_large_number():
    assert specialFilter([12345678911]) == 1