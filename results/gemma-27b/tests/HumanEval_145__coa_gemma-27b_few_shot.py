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
    assert order_by_points([1, 11, 2, 21]) == [1, 2, 11, 21]

def test_order_by_points_tie_breaking_negative():
    assert order_by_points([-1, -11, -2, -21]) == [-1, -2, -11, -21]

def test_order_by_points_tie_breaking_mixed():
    assert order_by_points([1, -1, 11, -11]) == [1, -1, 11, -11]