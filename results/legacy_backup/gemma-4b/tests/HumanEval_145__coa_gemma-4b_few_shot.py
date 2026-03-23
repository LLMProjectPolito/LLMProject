import pytest
import math


# Focus: Boundary Values
def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single():
    assert order_by_points([5]) == [5]

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

# Focus: Type Scenarios
def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_sum():
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

# Focus: Logic Branches
def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_duplicates():
    assert order_by_points([1, 11, 111, 1111]) == [1, 11, 111, 1111]