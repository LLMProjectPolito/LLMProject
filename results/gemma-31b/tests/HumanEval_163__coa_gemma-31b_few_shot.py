
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
import math


# Focus: Boundary Values
def test_generate_integers_boundary_min():
    # Test the smallest possible positive integer input
    assert generate_integers(1, 1) == []

def test_generate_integers_boundary_min_even():
    # Test the smallest even digit boundary
    assert generate_integers(2, 2) == [2]

def test_generate_integers_boundary_non_digit():
    # Test the boundary where integers are no longer single digits
    assert generate_integers(10, 10) == []

# Focus: Input Order
def test_input_order_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_input_order_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_input_order_equal():
    assert generate_integers(4, 4) == [4]

# Focus: Value Magnitude
def test_generate_integers_large_magnitude():
    # Testing values far beyond the single-digit range
    assert generate_integers(100, 1000) == []
    assert generate_integers(10000, 500) == []

def test_generate_integers_small_magnitude():
    # Testing the smallest positive integers
    assert generate_integers(1, 1) == []
    assert generate_integers(1, 2) == [2]

def test_generate_integers_full_digit_range():
    # Testing the maximum possible range of single digits
    assert generate_integers(1, 9) == [2, 4, 6, 8]