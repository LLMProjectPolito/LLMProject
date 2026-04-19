
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
    (2, 8, [2, 4, 6, 8]),    # Standard case ascending
    (8, 2, [2, 4, 6, 8]),    # Standard case descending
    (1, 5, [2, 4]),          # Range starting from 1
    (5, 1, [2, 4]),          # Range starting from 5 descending to 1
    (3, 7, [4, 6]),          # Mid range
    (7, 3, [4, 6]),          # Mid range reversed
    (10, 14, []),            # Range completely above single digits
    (100, 200, []),          # Large numbers
    (11, 15, []),            # No single digits in range
    (7, 12, [8]),            # Range overlapping the upper bound of digits
    (5, 12, [6, 8]),         # Range overlapping the upper bound of digits
    (12, 5, [6, 8]),         # Range overlapping the upper bound reversed
    (0, 3, [0, 2]),          # Range including zero
    (0, 12, [0, 2, 4, 6, 8]),# Range from zero to above single digits
    (4, 4, [4]),             # Single even digit range
    (3, 3, []),              # Single odd digit range
    (12, 12, []),            # Single value out of range
    (1, 9, [2, 4, 6, 8]),    # Full range of positive digits
    (0, 9, [0, 2, 4, 6, 8]), # Full range of non-negative digits
    (9, 11, []),             # Range spanning the edge of single digits (9, 10, 11)
])
def test_generate_integers(a, b, expected):
    """Test various ranges to ensure correct even single-digit integers are returned."""
    assert generate_integers(a, b) == expected

def test_generate_integers_type_return():
    """Ensure the function always returns a list."""
    result = generate_integers(2, 8)
    assert isinstance(result, list)

def test_generate_integers_ascending_order():
    """Ensure the output is always in ascending order regardless of input order."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(2, 8) == [2, 4, 6, 8]