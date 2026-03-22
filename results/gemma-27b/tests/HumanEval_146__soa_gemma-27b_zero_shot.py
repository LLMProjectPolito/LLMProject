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

def test_empty_array():
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
    assert specialFilter([101, 123, 157, 189, 1000]) == 0

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_with_one_odd_digit():
    assert specialFilter([12, 34, 56, 78, 90, 11, 33, 55, 77, 99]) == 4

def test_example_1():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_example_2():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_numbers_close_to_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_numbers_greater_than_10_with_even_first_digit():
    assert specialFilter([21, 43, 65, 87, 109]) == 0

def test_numbers_greater_than_10_with_even_last_digit():
    assert specialFilter([12, 34, 56, 78, 11]) == 0

def test_numbers_with_leading_zeros():
    assert specialFilter([011, 013, 015]) == 0

def test_numbers_with_trailing_zeros():
    assert specialFilter([110, 130, 150]) == 0