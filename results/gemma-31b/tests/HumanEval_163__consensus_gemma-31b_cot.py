
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
    (1, 9, [2, 4, 6, 8]),
    (1, 5, [2, 4]),
    (5, 1, [2, 4]),
    (3, 7, [4, 6]),
    
    # Single digit ranges
    (1, 3, [2]),
    (3, 5, [4]),
    (7, 9, [8]),
    (9, 7, [8]),
    (1, 2, [2]),
    (2, 1, [2]),
    
    # Single value boundaries
    (2, 2, [2]),
    (1, 1, []),
    (7, 7, []),
    (8, 8, [8]),
    (5, 5, []),
    (6, 6, [6]),
    (12, 12, []),
    
    # Zero and low boundary cases
    (0, 0, [0]),
    (0, 2, [0, 2]),
    (0, 4, [0, 2, 4]),
    (4, 0, [0, 2, 4]),
    (0, 9, [0, 2, 4, 6, 8]),
    
    # Ranges crossing or overlapping the digit boundary (10)
    (5, 15, [6, 8]),
    (15, 5, [6, 8]),
    (5, 12, [6, 8]),
    (12, 5, [6, 8]),
    (8, 15, [8]),
    (15, 8, [8]),
    
    # Ranges completely outside the single-digit range
    (10, 14, []),
    (11, 20, []),
    (20, 11, []),
    (100, 200, []),
    (15, 25, []),
    (11, 15, []),
    
    # Large bounds encompassing all digits
    (1, 1000, [2, 4, 6, 8]),
    (1000, 1, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests the generate_integers function with various edge cases including
    reversed ranges, ranges outside the 0-9 digit scope, and single-digit ranges.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type_consistency():
    """
    Ensure the function always returns a list.
    """
    result = generate_integers(10, 20)
    assert isinstance(result, list)