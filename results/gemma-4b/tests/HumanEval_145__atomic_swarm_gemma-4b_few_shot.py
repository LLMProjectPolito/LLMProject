import pytest
import math

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_empty():
    assert order_by_points([]) == []