
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
    (2, 8, [2, 4, 6, 8]),      # Standard ascending
    (8, 2, [2, 4, 6, 8]),      # Standard descending
    (10, 14, []),              # No digits in range (all > 9)
    (14, 10, []),              # No digits in range (descending)
    (4, 4, [4]),               # Single even digit
    (5, 5, []),                # Single odd digit
    (1, 1, []),                # Single odd digit (boundary)
    (1, 9, [2, 4, 6, 8]),      # Range covering multiple even digits
    (7, 9, [8]),               # Range at the end of digit scale
    (1, 3, [2]),               # Range at the start of digit scale
    (100, 200, []),            # Large numbers
    (1, 100, [2, 4, 6, 8]),    # Large range including all digits
])
def test_generate_integers(a, b, expected):
    """
    Tests the generate_integers function with various scenarios including
    ascending/descending ranges, ranges with no digits, and single-element ranges.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type_consistency():
    """
    Ensures the function returns a list even when no even digits are found.
    """
    result = generate_integers(10, 20)
    assert isinstance(result, list)
    assert len(result) == 0

def test_generate_integers_order():
    """
    Explicitly verifies that the output is always in ascending order.
    """
    # Even if input is descending, output must be [2, 4, 6]
    result = generate_integers(6, 2)
    assert result == [2, 4, 6]
    assert result == sorted(result)