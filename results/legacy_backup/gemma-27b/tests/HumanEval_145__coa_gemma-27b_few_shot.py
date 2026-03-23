import pytest
import math


# Focus: Digit Sum Calculation
import pytest

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_same_digit_sum():
    assert order_by_points([12, 21, 3, 30]) == [3, 12, 21, 30]

# Focus: Empty/Null Input
def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_null():
    assert order_by_points(None) == None

# Focus: Tie-breaking with Original Index
import pytest

def test_order_by_points_tie_breaking():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_tie_breaking_multiple():
    assert order_by_points([12, 21, 3, 30, 1, 10]) == [1, 10, 3, 12, 21, 30]

def test_order_by_points_tie_breaking_all_same():
    assert order_by_points([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]