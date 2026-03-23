import pytest
import math

def test_specialFilter_typical_case():
    nums = [33, -2, -3, 45, 21, 109]
    assert specialFilter(nums) == 2

def test_specialFilter_empty_list():
    """Test with an empty list."""
    assert specialFilter([]) == 0

def test_specialFilter_invalid_input():
    """Test with a list containing a string."""
    nums = [15, -73, "abc", -15]
    try:
        from main import specialFilter
        specialFilter(nums)
    except TypeError as e:
        assert isinstance(e, TypeError), "Expected TypeError, but got a different exception."
    else:
        assert False, "TypeError was not raised for invalid input."