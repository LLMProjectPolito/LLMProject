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

def test_empty_list():
    assert specialFilter([]) == 0

def test_no_elements_satisfying_conditions():
    assert specialFilter([-1, -2, -3]) == 0

def test_some_elements_satisfying_conditions():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_all_elements_satisfying_conditions():
    assert specialFilter([11, 13, 15, 17, 19]) == 5

def test_mixed_elements():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers_and_elements_satisfying_conditions():
    assert specialFilter([-11, -13, 15, -17, 19]) == 3

def test_list_with_zero():
    assert specialFilter([10, 11]) == 0

def test_large_numbers():
    assert specialFilter([101, 103, 105, 107, 109]) == 5

def test_single_element_satisfying_conditions():
    assert specialFilter([11]) == 1

def test_single_element_not_satisfying_conditions():
    assert specialFilter([10]) == 0

def test_negative_single_element_satisfying_conditions():
    assert specialFilter([-11]) == 1

def test_negative_single_element_not_satisfying_conditions():
    assert specialFilter([-10]) == 0