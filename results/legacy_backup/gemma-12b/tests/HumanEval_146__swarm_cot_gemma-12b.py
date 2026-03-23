import pytest
import math

def test_specialFilter_empty_list():
    """Test with an empty list."""
    from solution import specialFilter
    assert specialFilter([]) == 0

def test_specialFilter_no_numbers_greater_than_10():
    """Test with numbers less than or equal to 10."""
    from solution import specialFilter
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

def test_specialFilter_negative_numbers_with_odd_digits():
    """Test with negative numbers that meet the criteria."""
    from solution import specialFilter
    assert specialFilter([-15, -33, -57, -79]) == 0

def test_specialFilter_large_number_with_odd_digits():
    """Test with a large number that meets the criteria."""
    from solution import specialFilter
    assert specialFilter([13579]) == 0

def test_specialFilter_edge_case_11():
    """Test with 11, which is greater than 10 but doesn't fit the odd digit criteria."""
    from solution import specialFilter
    assert specialFilter([11]) == 0

def test_specialFilter_edge_case_13():
    """Test with a number that is just above the threshold and has odd digits."""
    from solution import specialFilter
    assert specialFilter([13]) == 0

def test_specialFilter_edge_case_15():
    """Test with a number that is just above the threshold and has odd digits."""
    from solution import specialFilter
    assert specialFilter([15]) == 1

def test_specialFilter_edge_case_17():
    """Test with a number that is just above the threshold and has odd digits."""
    from solution import specialFilter
    assert specialFilter([17]) == 1

def test_specialFilter_edge_case_19():
    """Test with a number that is just above the threshold and has odd digits."""
    from solution import specialFilter
    assert specialFilter([19]) == 1

def test_specialFilter_mixed_positive_and_negative_odd_digits():
    """Test with a mix of positive and negative numbers with odd digits."""
    from solution import specialFilter
    assert specialFilter([15, -73, 14, -15, 35, -57, 79, -91]) == 3

def test_specialFilter_edge_case_101():
    """Test with 101, which is greater than 10 and has odd first and last digits."""
    from solution import specialFilter
    assert specialFilter([101]) == 1

def test_specialFilter_mixed_positive_and_negative():
    """Test with a mix of positive and negative numbers."""
    from solution import specialFilter
    assert specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109, -91]) == 2