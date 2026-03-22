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
    assert specialFilter([101, 123, 157, 189, 10001]) == 4

def test_numbers_with_even_digits():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_numbers_close_to_10():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_numbers_greater_than_10_with_odd_first_and_last():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_numbers_greater_than_10_with_even_first_or_last():
    assert specialFilter([12, 34, 56, 78, 90]) == 0

def test_mixed_positive_and_negative():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_edge_case_11():
    assert specialFilter([11]) == 1

def test_edge_case_99():
    assert specialFilter([99]) == 1

def test_edge_case_101():
    assert specialFilter([101]) == 1

def test_edge_case_1001():
    assert specialFilter([1001]) == 1