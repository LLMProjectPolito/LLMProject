
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
import math


# Focus: Boundary Values
def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(-1) == (0, 1)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(-2) == (1, 0)

# Focus: Negative Values
def test_even_odd_count_negative_mixed():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-12345) == (2, 3)

def test_even_odd_count_negative_all_even():
    assert even_odd_count(-2468) == (4, 0)
    assert even_odd_count(-20) == (2, 0)

def test_even_odd_count_negative_all_odd():
    assert even_odd_count(-1357) == (0, 4)
    assert even_odd_count(-9) == (0, 1)

# Focus: Digit Composition
def test_even_odd_composition_mixed():
    assert even_odd_count(12345) == (2, 3)
    assert even_odd_count(24681357) == (4, 4)
    assert even_odd_count(-102) == (2, 1)

def test_even_odd_composition_uniform():
    assert even_odd_count(246) == (3, 0)
    assert even_odd_count(135) == (0, 3)
    assert even_odd_count(-888) == (3, 0)

def test_even_odd_composition_single_digit():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(-4) == (1, 0)