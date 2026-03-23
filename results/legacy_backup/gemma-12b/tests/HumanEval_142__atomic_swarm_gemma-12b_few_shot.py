import pytest
import math

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3, 4, 5]) == 17

def test_sum_squares_all_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_wrong_type():
    assert sum_squares([1, 2, "a"]) == 0