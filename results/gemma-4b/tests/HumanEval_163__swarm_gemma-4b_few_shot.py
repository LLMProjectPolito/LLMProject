
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

def generate_integers(start, end):
    """Generates a list of odd integers within a given range."""
    odd_numbers = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []

def test_generate_integers_no_even_2():
    assert generate_integers(1, 3) == []

def test_generate_integers_no_even_3():
    assert generate_integers(1, 3) == []

def test_generate_integers_with_odd():
    assert generate_integers(1, 5) == [1, 3, 5]

def test_generate_integers_empty():
    assert generate_integers(2, 2) == []

def test_generate_integers_single():
    assert generate_integers(1, 1) == [1]