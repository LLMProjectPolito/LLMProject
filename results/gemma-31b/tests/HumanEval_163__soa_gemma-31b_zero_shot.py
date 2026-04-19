
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
    (10, 14, []),            # Range entirely above single digits
    (1, 3, [2]),             # Small range with one even digit
    (1, 1, []),              # Single odd digit
    (2, 2, [2]),             # Single even digit
    (5, 7, [6]),             # Range with one even digit in middle
    (1, 11, [2, 4, 6, 8]),   # Range spanning into double digits
    (11, 1, [2, 4, 6, 8]),   # Range spanning into double digits, reversed
    (3, 5, [4]),             # Range with one even digit
    (7, 9, [8]),             # Range with one even digit
    (9, 10, []),             # Range crossing into double digits with no even digits in [9, 9]
    (0, 9, [0, 2, 4, 6, 8]), # Including zero if treated as a positive/non-negative integer
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_no_evens():
    """Test range containing only odd digits."""
    assert generate_integers(1, 1) == []
    assert generate_integers(3, 3) == []
    assert generate_integers(1, 1) == []

def test_generate_integers_large_values():
    """Test ranges where both values are significantly larger than 9."""
    assert generate_integers(100, 200) == []
    assert generate_integers(200, 100) == []