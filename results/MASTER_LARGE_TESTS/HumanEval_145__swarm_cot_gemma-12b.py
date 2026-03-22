import pytest
import math

def test_order_by_points_with_large_numbers():
    """Tests the function with large numbers to ensure digit sum calculation is correct."""
    nums = [1000000, 1, 1000, 10]
    expected = [1, 10, 1000, 1000000]
    assert order_by_points(nums) == expected