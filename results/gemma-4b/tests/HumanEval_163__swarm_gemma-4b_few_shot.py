
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
    """
    Generates a list of odd integers within a given range (inclusive).
    """
    odd_integers = []
    for i in range(start, end + 1):
        if i % 2 != 0:
            odd_integers.append(i)
    return odd_integers

def test_generate_integers_no_even():
    assert generate_integers(11, 13) == []

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []