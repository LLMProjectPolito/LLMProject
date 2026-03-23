import pytest

def test_order_by_points_negative_and_positive():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]