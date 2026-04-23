
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_specialFilter_empty_array():
    """Test with an empty array."""
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    """Test with an array containing numbers greater than 10, but not meeting the digit criteria."""
    assert specialFilter([11, 12, 13, 14]) == 0
    assert specialFilter([11, 12, 13, 14, 15]) == 0

def test_specialFilter_negative_numbers():
    """Test with negative numbers that meet the criteria."""
    assert specialFilter([-15, -33, -55]) == 0

def test_specialFilter_single_matching_number():
    """Test with a single number that meets the criteria."""
    assert specialFilter([35]) == 1

def test_specialFilter_multiple_matching_numbers():
    """Test with multiple numbers that meet the criteria."""
    assert specialFilter([35, 79, 11, 13, 15, 17, 19]) == 4
    assert specialFilter([15, 22, 35, 44, 57]) == 2

def test_specialFilter_mixed_numbers():
    """Test with a mix of numbers, some meeting the criteria, some not."""
    assert specialFilter([15, -73, 14, -15, 33, 2, -3, 45, 21, 109, 111]) == 4

def test_specialFilter_large_numbers():
    """Test with large numbers to ensure digit extraction works correctly."""
    assert specialFilter([3579, 1111, 1234, 5678]) == 1
    assert specialFilter([151, 353, 575, 797]) == 4

def test_specialFilter_zero():
    """Test with zero."""
    assert specialFilter([0]) == 0

def test_specialFilter_edge_case_1():
    """Test with a number where the first digit is odd and the last digit is even."""
    assert specialFilter([12]) == 0

def test_specialFilter_edge_case_2():
    """Test with a number where the first digit is even and the last digit is odd."""
    assert specialFilter([21]) == 0

def test_specialFilter_mixed_positive_and_negative():
    """Test with a mix of positive and negative numbers."""
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_edge_case_11():
    """Test with a number where both digits are the same and odd."""
    assert specialFilter([11]) == 0

def test_specialFilter_edge_case_101():
    """Test with a number where the first and last digits are odd, but the middle digit is even."""
    assert specialFilter([101]) == 0