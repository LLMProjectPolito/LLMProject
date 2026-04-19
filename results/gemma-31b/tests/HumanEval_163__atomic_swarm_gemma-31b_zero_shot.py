
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

def test_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_out_of_digit_range():
    assert generate_integers(10, 10) == []

import pytest

def test_generate_integers_wrong_type():
    with pytest.raises(TypeError):
        generate_integers("2", 8)