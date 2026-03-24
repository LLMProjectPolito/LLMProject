
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

def test_basic_ascending():
    """Checks basic ascending range with even numbers."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_basic_descending():
    """Checks basic descending range with even numbers."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_mixed_even_odd():
    """Checks a range with mixed even and odd numbers."""
    assert generate_integers(3, 9) == [4, 6, 8]

def test_no_even_numbers():
    """Checks a range with no even numbers."""
    assert generate_integers(1, 3) == []
    assert generate_integers(3, 5) == []

def test_single_even_number():
    """Checks a range with a single even number."""
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 4) == [4]

def test_same_number_even():
    """Checks the case where a and b are equal and even."""
    assert generate_integers(4, 4) == [4]
    assert generate_integers(6, 6) == [6]

def test_same_number_odd():
    """Checks the case where a and b are equal and odd."""
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []

def test_edge_case_zero():
    """Checks edge cases involving zero."""
    assert generate_integers(0, 2) == [2]
    assert generate_integers(2, 0) == [2]
    assert generate_integers(0, 0) == []

def test_large_numbers():
    """Checks a range with large numbers."""
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_negative_numbers():
    """Checks a range with negative numbers."""
    assert generate_integers(-2, 2) == [-2, 0, 2]

def test_a_greater_than_b():
    """Checks if the function handles the case where a is greater than b correctly."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 4) == [4, 6, 8, 10]
    assert generate_integers(14, 6) == [6, 8, 10, 12, 14]