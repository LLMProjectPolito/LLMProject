
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
    (8, 12, [8]),
    (4, 4, [4]),
    (6, 6, [6]),
])
def test_generate_integers(start, end, expected):
    assert generate_integers(start, end) == expected