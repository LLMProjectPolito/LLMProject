import pytest
import math

def test_order_by_points_positive():
    nums = [1, 11, -1, -11, -12]
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == expected

def test_empty_input():
    assert order_by_points([]) == []

def test_order_by_points_wrong_type():
    """Test with a list containing a string."""
    try:
        order_by_points([1, 2, "a"])
    except TypeError:
        assert True
    else:
        assert False