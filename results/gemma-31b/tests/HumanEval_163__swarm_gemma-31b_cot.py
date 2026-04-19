
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

@pytest.mark.parametrize("start, end, expected", [
    (8, 12, [8]),    # Digit boundary: only 8 is an even single digit
    (5, 100, [6, 8]), # Partial overlap: only single-digit even integers
    (12, 8, [8]),    # Reverse range: ensures ascending order and digit constraint
])
def test_generate_integers_digit_constraints(start, end, expected):
    """Tests that generate_integers only returns even single-digit integers (0-9)."""
    assert generate_integers(start, end) == expected