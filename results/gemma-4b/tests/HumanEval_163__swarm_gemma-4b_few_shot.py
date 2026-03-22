import pytest
import math

def generate_integers(start, end):
    """
    Generates a list of odd integers within a given range (inclusive).
    """
    odd_integers = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            odd_integers.append(i)
    return odd_integers

def test_generate_integers_no_even():
    assert generate_integers(11, 13) == [11, 13]

def test_generate_integers_empty_range():
    assert generate_integers(10, 10) == []

def test_generate_integers_single_odd():
    assert generate_integers(7, 7) == [7]

def test_generate_integers_multiple_odd():
    assert generate_integers(1, 5) == [1, 3, 5]

def test_generate_integers_negative_range():
    assert generate_integers(-5, -3) == [-5, -3]