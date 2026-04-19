
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
    (2, 8, [2, 4, 6, 8]),    # Standard range ascending
    (8, 2, [2, 4, 6, 8]),    # Standard range descending
    (10, 14, []),            # Range with even numbers but no even digits
    (1, 1, []),              # Single odd number
    (2, 2, [2]),             # Single even digit
    (3, 5, [4]),             # Range containing one even digit
    (1, 9, [2, 4, 6, 8]),    # Full range of positive even digits
    (5, 12, [6, 8]),         # Range spanning digits and multi-digit numbers
    (15, 20, []),            # Range entirely above single digits
    (7, 7, []),              # Single odd digit
    (0, 4, [0, 2, 4]),       # Range including zero (if treated as positive/non-negative)
    (100, 200, []),          # Large numbers
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected