
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
def test_generate_integers_boundary_equal_even():
    # Boundary: a and b are the same even digit
    assert generate_integers(4, 4) == [4]

def test_generate_integers_boundary_edge_of_digits():
    # Boundary: range spans the upper limit of single digits (9)
    assert generate_integers(8, 10) == [8]

def test_generate_integers_boundary_just_outside():
    # Boundary: range starts exactly where single digits end
    assert generate_integers(10, 12) == []

# Focus: Logic Branches
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_equal():
    assert generate_integers(4, 4) == [4]
    assert generate_integers(3, 3) == []

# Focus: Value Ranges
import pytest

def test_value_ranges_no_even_digits():
    # Range containing only odd digits or a single odd digit
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(1, 1) == []

def test_value_ranges_all_even_digits():
    # Range covering all possible even digits (2, 4, 6, 8)
    assert generate_integers(1, 9) == [2, 4, 6, 8]
    assert generate_integers(9, 1) == [2, 4, 6, 8]

def test_value_ranges_out_of_digit_bounds():
    # Range entirely above the single-digit range
    assert generate_integers(11, 20) == []
    assert generate_integers(20, 11) == []