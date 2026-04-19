
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
    # Basic cases from docstring
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Single digit ranges
    (1, 3, [2]),
    (3, 1, [2]),
    (1, 9, [2, 4, 6, 8]),
    (9, 1, [2, 4, 6, 8]),
    
    # Ranges that partially overlap with single digits
    (5, 12, [6, 8]),
    (12, 5, [6, 8]),
    (0, 4, [0, 2, 4]),
    (7, 15, [8]),
    (15, 7, [8]),
    
    # Ranges completely outside single digits
    (11, 20, []),
    (20, 11, []),
    
    # Edge cases: a == b
    (2, 2, [2]),
    (3, 3, []),
    (8, 8, [8]),
    (10, 10, []),
    
    # Edge cases: no even digits in range
    (1, 1, []),
    (3, 5, [4]),
    (5, 5, []),
    (7, 7, []),
    (9, 9, []),
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected