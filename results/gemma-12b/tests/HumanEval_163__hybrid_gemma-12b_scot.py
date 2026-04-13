
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest
from your_module import generate_integers  # Replace your_module

def test_ascending_order():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_descending_order():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_empty_range():
    assert generate_integers(10, 14) == []

def test_single_even():
    assert generate_integers(2, 3) == [2]

def test_multiple_evens():
    assert generate_integers(4, 10) == [4, 6, 8, 10]

def test_inclusive_bounds():
    assert generate_integers(2, 6) == [2, 4, 6]

def test_negative_numbers():
    assert generate_integers(-2, 2) == []
    assert generate_integers(-5, -1) == []

def test_zero_and_positive():
    assert generate_integers(0, 4) == [0, 2, 4]

def test_same_numbers_even():
    assert generate_integers(4, 4) == [4]

def test_same_numbers_odd():
    assert generate_integers(3, 3) == []

def test_mixed_even_odd():
    assert generate_integers(3, 9) == [4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(1, 3) == []

def test_large_numbers():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_edge_case_zero():
    assert generate_integers(0, 4) == [0, 2, 4]