import pytest
import math

def test_specialFilter_positive():
    nums = [33, -2, -3, 45, 21, 109]
    assert specialFilter(nums) == 2

def test_empty_input():
    """Test with an empty input list."""
    assert specialFilter([]) == 0

def test_specialFilter_empty_list():
    """Test with an empty list."""
    assert specialFilter([]) == 0