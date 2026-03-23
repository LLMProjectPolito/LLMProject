import pytest
import math

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_all_negative():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_order_by_points_mixed_types():
    assert order_by_points([1, "a", 2]) == [1, 2, "a"]