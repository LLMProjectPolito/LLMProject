import pytest
import math

def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_all_correct():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_compare_wrong_length():
    assert compare([1, 2, 3], [1, 2]) == [0, 0, 3]