
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

def test_generate_integers_positive():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_edge_empty_range():
    assert generate_integers(5, 5) == []

def test_generate_integers_invalid_input_types():
    """Test with non-integer inputs."""
    try:
        generate_integers(2.5, 8)
        assert False, "TypeError not raised for float input"
    except TypeError:
        pass

    try:
        generate_integers("2", 8)
        assert False, "TypeError not raised for string input"
    except TypeError:
        pass