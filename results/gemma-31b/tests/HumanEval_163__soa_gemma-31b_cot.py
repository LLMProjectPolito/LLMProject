
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
    (10, 14, []),            # Range entirely above single digits
    (1, 1, []),              # Single odd number
    (2, 2, [2]),             # Single even digit
    (1, 3, [2]),             # Range containing one even digit
    (5, 7, [6]),             # Range containing one even digit
    (1, 9, [2, 4, 6, 8]),    # Full range of positive digits
    (9, 1, [2, 4, 6, 8]),    # Full range of positive digits reversed
    (7, 12, [8]),            # Range crossing the digit boundary (only 8 is an even digit)
    (15, 20, []),            # Range far beyond digits
    (0, 4, [0, 2, 4]),       # Including zero (if considered positive/non-negative)
    (4, 0, [0, 2, 4]),       # Including zero reversed
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected