
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
    # Provided examples
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Edge cases: Single number ranges
    (2, 2, [2]),
    (3, 3, []),
    (0, 0, [0]),
    
    # Edge cases: Range boundaries
    (0, 9, [0, 2, 4, 6, 8]),
    (9, 0, [0, 2, 4, 6, 8]),
    (1, 9, [2, 4, 6, 8]),
    
    # Edge cases: Partial overlap with digit range (0-9)
    (7, 12, [8]),
    (12, 7, [8]),
    (-2, 2, [0, 2]), # Testing behavior with non-positive integers if passed
    (5, 6, [6]),
    
    # Edge cases: No even digits in range
    (1, 1, []),
    (11, 13, []),
    (15, 19, []),
    
    # Edge cases: Large numbers
    (100, 200, []),
    (1000, 1000, []),
    
    # Edge cases: Range containing only odd digits
    (1, 3, [2]),
    (3, 5, [4]),
    (7, 9, [8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests the generate_integers function against various scenarios including
    standard ranges, reversed ranges, ranges outside the digit scope,
    and boundary conditions.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type_consistency():
    """
    Ensure the function always returns a list, even when empty.
    """
    result = generate_integers(11, 15)
    assert isinstance(result, list)

def test_generate_integers_ascending_order():
    """
    Explicitly verify that the output is always in ascending order regardless of input order.
    """
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(2, 8) == [2, 4, 6, 8]