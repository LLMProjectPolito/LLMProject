
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

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (1, 3, [2]),
    (1, 1, []),
    (4, 4, [4]),
    (1, 9, [2, 4, 6, 8]),
    (0, 9, [0, 2, 4, 6, 8]),
    (5, 7, [6]),
    (11, 20, []),
    (2, 2, [2]),
    (3, 3, []),
    (1, 100, [2, 4, 6, 8]),
    (100, 1, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected