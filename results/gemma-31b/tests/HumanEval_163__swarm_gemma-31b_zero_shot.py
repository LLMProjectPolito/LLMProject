
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

def test_generate_integers_partial_range():
    assert generate_integers(5, 15) == [6, 8]

def test_generate_integers_cross_ten():
    assert generate_integers(7, 12) == [8]