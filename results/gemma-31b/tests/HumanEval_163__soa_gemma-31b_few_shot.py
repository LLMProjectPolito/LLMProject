
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
    (2, 8, [2, 4, 6, 8]),    # Standard range
    (8, 2, [2, 4, 6, 8]),    # Reversed range
    (10, 14, []),            # Range above digits
    (1, 1, []),              # Single odd digit
    (2, 2, [2]),             # Single even digit
    (1, 3, [2]),             # Range containing one even digit
    (3, 7, [4, 6]),          # Range containing multiple even digits, starting/ending odd
    (0, 9, [0, 2, 4, 6, 8]), # Range covering all digits (if 0 is considered)
    (1, 9, [2, 4, 6, 8]),    # Range covering all positive digits
    (5, 5, []),              # Single odd number
    (100, 200, []),          # Large numbers
    (4, 6, [4, 6]),          # Inclusive boundaries
    (7, 9, [8]),             # End of digit range
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected