
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

@pytest.mark.parametrize("a, b, expected", [
    (6, 6, [6]),
    (2, 2, [2]),
])
def test_generate_integers_identical_even_bounds(a, b, expected):
    """Test that the function returns a single even digit when a and b are the same even digit."""
    assert generate_integers(a, b) == expected

def test_generate_integers_boundary_overlap():
    """
    Tests that the function correctly filters out even numbers that are 
    not single digits when the range spans across the 9-10 boundary.
    """
    assert generate_integers(8, 12) == [8]