
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
    # Standard ranges
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (1, 5, [2, 4]),
    (5, 1, [2, 4]),
    (3, 7, [4, 6]),
    (7, 3, [4, 6]),
    (4, 6, [4, 6]),
    (6, 4, [4, 6]),
    (5, 7, [6]),
    (7, 5, [6]),
    (7, 9, [8]),
    (9, 7, [8]),
    
    # Full single-digit range
    (1, 9, [2, 4, 6, 8]),
    (9, 1, [2, 4, 6, 8]),
    
    # Boundary cases with 0
    (0, 4, [0, 2, 4]),
    (4, 0, [0, 2, 4]),
    (0, 2, [0, 2]),
    (2, 0, [0, 2]),
    
    # Partial overlap with single-digit range
    (5, 15, [6, 8]),
    (15, 5, [6, 8]),
    (2, 12, [2, 4, 6, 8]),
    (12, 2, [2, 4, 6, 8]),
    (8, 15, [8]),
    (15, 8, [8]),
    
    # Single value ranges (a == b)
    (2, 2, [2]),
    (4, 4, [4]),
    (3, 3, []),
    (1, 1, []),
    (10, 10, []),
    (11, 11, []),
    
    # Ranges entirely outside single-digit range
    (10, 14, []),
    (14, 10, []),
    (11, 13, []),
    (13, 11, []),
    (15, 25, []),
    (100, 200, []),
    
    # Large ranges
    (1, 1000, [2, 4, 6, 8]),
    (1000, 1, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests the generate_integers function to ensure it returns all even single-digit 
    integers within the inclusive range [min(a, b), max(a, b)] in ascending order.
    """
    assert generate_integers(a, b) == expected