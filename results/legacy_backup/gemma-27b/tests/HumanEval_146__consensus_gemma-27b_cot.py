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
    assert specialFilter([15, 37, 59]) == 3

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_negative_numbers():
    assert specialFilter([-11, -13, -15]) == 3

def test_large_numbers():
    assert specialFilter([101, 123, 155, 179]) == 4

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78]) == 0

def test_numbers_close_to_10():
    assert specialFilter([11, 99, 10, 12]) == 2

def test_example_1():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_all_numbers_greater_than_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_numbers_with_leading_zeros():
    assert specialFilter([101, 103, 105]) == 3

def test_numbers_with_trailing_zeros():
    assert specialFilter([110, 130, 150]) == 0

def test_numbers_with_both_leading_and_trailing_zeros():
    assert specialFilter([1001, 1003, 1005]) == 3

def test_numbers_with_multiple_digits():
    assert specialFilter([123, 345, 567, 789]) == 2

def test_numbers_with_negative_sign():
    assert specialFilter([-11, -13, -15, -17, -19]) == 5

def test_numbers_with_mixed_signs():
    assert specialFilter([11, -13, 15, -17, 19]) == 4