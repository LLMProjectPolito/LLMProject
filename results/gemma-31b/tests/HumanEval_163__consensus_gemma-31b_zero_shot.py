
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
    (2, 8, [2, 4, 6, 8]),    # Standard range, ascending
    (8, 2, [2, 4, 6, 8]),    # Standard range, descending
    (1, 9, [2, 4, 6, 8]),    # Full digit range
    (1, 10, [2, 4, 6, 8]),   # Range including upper boundary of digits
    (10, 1, [2, 4, 6, 8]),   # Range including upper boundary of digits, reversed
    (10, 14, []),            # Range entirely above single digits
    (11, 15, []),            # Range above digits
    (100, 200, []),          # Large values out of range
    (200, 100, []),          # Large values out of range reversed
    (5, 15, [6, 8]),         # Range overlapping digits and non-digits
    (15, 5, [6, 8]),         # Range overlapping digits and non-digits, reversed
    (8, 12, [8]),            # Partial overlap
    (12, 8, [8]),            # Partial overlap reversed
    (100, 1, [2, 4, 6, 8]),  # Large range covering all digits
    (100, 5, [6, 8]),        # Large range partial overlap
    (1, 1, []),              # Single odd number
    (2, 2, [2]),             # Single even digit
    (3, 3, []),              # Single odd digit
    (10, 10, []),            # Single non-digit
    (1, 2, [2]),             # Small range
    (3, 5, [4]),             # Middle of digit range
    (7, 9, [8]),             # Single even digit in range
    (0, 9, [0, 2, 4, 6, 8]), # Testing 0 as an even digit
    (0, 2, [0, 2]),          # Testing 0 boundary
])
def test_generate_integers_parametrized(a, b, expected):
    """Comprehensive test suite for generate_integers covering various ranges and edge cases."""
    assert generate_integers(a, b) == expected

def test_generate_integers_odd_boundaries():
    """Test range where boundaries are odd numbers."""
    assert generate_integers(1, 7) == [2, 4, 6]
    assert generate_integers(7, 1) == [2, 4, 6]

def test_generate_integers_no_evens():
    """Test ranges that contain only odd digits."""
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(7, 7) == []