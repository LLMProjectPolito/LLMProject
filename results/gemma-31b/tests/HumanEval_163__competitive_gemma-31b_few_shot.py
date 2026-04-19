
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
    (2, 8, [2, 4, 6, 8]),    # Example 1: Standard range
    (8, 2, [2, 4, 6, 8]),    # Example 2: Reversed range
    (10, 14, []),            # Example 3: Range above single digits
    (1, 1, []),              # Single odd number
    (2, 2, [2]),             # Single even number
    (1, 3, [2]),             # Range containing one even digit
    (1, 9, [2, 4, 6, 8]),    # Range containing all even digits
    (9, 1, [2, 4, 6, 8]),    # Range containing all even digits reversed
    (1, 11, [2, 4, 6, 8]),   # Upper bound above 9
    (11, 1, [2, 4, 6, 8]),   # Lower bound above 9
    (5, 7, [6]),             # Range with one even digit in middle
    (3, 5, [4]),             # Range with one even digit in middle
    (7, 9, [8]),             # Range with one even digit at end
    (12, 15, []),            # Both bounds above 9
    (10, 2, [2, 4, 6, 8]),   # One bound above 9, reversed
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected