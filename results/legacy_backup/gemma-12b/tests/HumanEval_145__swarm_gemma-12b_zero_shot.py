import pytest
import math

def test_order_by_points_with_large_numbers():
    nums = [1000, 10, 1, 100]
    expected = [1, 10, 100, 1000]
    assert order_by_points(nums) == expected