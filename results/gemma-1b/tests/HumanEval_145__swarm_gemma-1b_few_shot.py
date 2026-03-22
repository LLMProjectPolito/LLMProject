import pytest
from math import sqrt

def order_by_points(points):
    """
    Sorts a list of points based on their x-coordinates.
    """
    if not points:
        return []
    return sorted(points)

def test_order_by_points():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

def test_order_by_points():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

def test_order_by_points():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

def test_order_by_points_large_numbers():
    assert order_by_points([1000, 1, 1001, -1, -1001]) == [-1, 1, 1001, 1000, -1]
    assert order_by_points([-1000, -1, -1001, 1, 1001]) == [-1, -1001, 1, 1001, -1000]
    assert order_by_points([1000, -1000, 1, -1, 1001]) == [-1, 1, 1000, -1000, 1001]
    assert order_by_points([-1000, 1000, -1, 1, -1001]) == [-1, 1, -1001, 1000, -1000]
    assert order_by_points([1000, -1000, 1001, -1, 1001]) == [-1, 1, 1001, -1001, 1000]