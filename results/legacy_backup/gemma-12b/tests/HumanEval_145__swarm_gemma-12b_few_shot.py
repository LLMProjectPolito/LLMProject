import pytest
import math

def test_order_by_points_with_zeros():
    assert order_by_points([0, 10, 1, -10, -1]) == [0, -1, 1, -10, 10]