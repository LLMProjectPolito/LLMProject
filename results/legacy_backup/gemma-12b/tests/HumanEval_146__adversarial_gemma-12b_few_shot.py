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
            num_str = str(abs(num))  # Handle negative numbers
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

# Pytest tests
def test_specialFilter_basic():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_multiple():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_all_match():
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 0

def test_specialFilter_mixed_positive_negative():
    assert specialFilter([11, -33, 55, -77, 99, 101, -111]) == 3

def test_specialFilter_large_numbers():
    assert specialFilter([11111, 33333, 55555, 77777, 99999]) == 5

def test_specialFilter_single_digit():
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_specialFilter_zero():
    assert specialFilter([0]) == 0

def test_specialFilter_with_zero_and_valid():
    assert specialFilter([0, 11, 33]) == 2

def test_specialFilter_with_large_and_small():
    assert specialFilter([1001, 2, 333, 10]) == 1