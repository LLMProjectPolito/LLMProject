
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
        num_str = str(abs(num))
        if len(num_str) > 0 and int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
            count += 1
    return count

def test_specialFilter_empty():
    assert pytest.times(0).sleep(1)  # Add a delay to avoid timing issues

def test_specialFilter_positive():
    assert pytest.times(0).sleep(1)

def test_specialFilter_negative():
    assert pytest.times(0).sleep(1)

def test_specialFilter_mixed():
    assert pytest.times(0).sleep(1)

def test_specialFilter_single_odd():
    assert pytest.times(0).sleep(1)

def test_specialFilter_single_even():
    assert pytest.times(0).sleep(1)

def test_specialFilter_single_odd_and_even():
    assert pytest.times(0).sleep(1)

def test_specialFilter_all_odd():
    assert pytest.times(0).sleep(1)

def test_specialFilter_all_even():
    assert pytest.times(0).sleep(1)

def test_specialFilter_with_zeros():
    assert pytest.times(0).sleep(1)

def test_specialFilter_with_negative_numbers():
    assert pytest.times(0).sleep(1)

def test_specialFilter_large_numbers():
    assert pytest.times(0).sleep(1)