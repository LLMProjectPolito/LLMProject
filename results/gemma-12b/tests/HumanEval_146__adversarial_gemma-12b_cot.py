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
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_numbers_greater_than_10():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_no_odd_first_and_last_digits():
    assert specialFilter([22, 44, 66, 88]) == 0

def test_mixed_numbers():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_positive_and_negative_numbers():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_large_numbers():
    assert specialFilter([123, 357, 911, 246]) == 2

def test_single_digit_numbers():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_numbers_with_zero():
    assert specialFilter([10, 30, 50, 70, 90]) == 0

def test_numbers_with_leading_zeros():
    assert specialFilter([15, -73, 14, -15, 101]) == 1

def test_all_numbers_satisfying_condition():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_negative_numbers_with_odd_digits():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_edge_case_11():
    assert specialFilter([11]) == 1

def test_edge_case_33():
    assert specialFilter([33]) == 1

def test_edge_case_55():
    assert specialFilter([55]) == 1

def test_edge_case_77():
    assert specialFilter([77]) == 1

def test_edge_case_99():
    assert specialFilter([99]) == 1