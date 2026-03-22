import pytest
import math

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_wrong_type():
    assert double_the_difference([1, 2.5, "a", 3]) == 1 + 9