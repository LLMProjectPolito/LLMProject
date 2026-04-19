
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
def test_generate_integers_boundary_same_even():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_boundary_same_odd():
    assert generate_integers(1, 1) == []

def test_generate_integers_boundary_out_of_range():
    assert generate_integers(10, 10) == []

# Focus: Logic Branches
def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

# Focus: Value Scenarios
def test_generate_integers_full_digit_range():
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_out_of_bounds():
    assert generate_integers(10, 20) == []

def test_generate_integers_single_even_digit():
    assert generate_integers(3, 5) == [4]