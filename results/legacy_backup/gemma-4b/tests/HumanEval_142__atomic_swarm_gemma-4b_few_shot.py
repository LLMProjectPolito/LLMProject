import pytest
import math

def test_sum_squares_basic():
    lst = [1, 2, 3]
    result = sum_squares(lst)
    assert result == 6

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_empty():
    assert sum_squares([]) == 0