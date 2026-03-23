import pytest
import math


# Focus: Index-based Calculations
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_mixed():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_longer_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 605

# Focus: Empty List/Null Input
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_null():
    assert sum_squares(None) == 0

# Focus: Positive/Negative/Zero Integers
def test_sum_squares_positive():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 64 + 5 + 36
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 9 + 100 + 11 + 1728

def test_sum_squares_negative():
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == -1 + -2 + 9 + -64 + -5 + 36
    assert sum_squares([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]) == -1 + -2 + 9 + -64 + -5 + 36 + -7 + -512 + -9 + 100 + -11 + 1728

def test_sum_squares_zero():
    assert sum_squares([0, 0, 0, 0, 0, 0]) == 0
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 0 + 1 + 2 + 9 + 4 + 5