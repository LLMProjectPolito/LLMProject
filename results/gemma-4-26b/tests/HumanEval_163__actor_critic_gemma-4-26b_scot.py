
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
    (1, 5, [2, 4]),            # Range within digits
    (5, 1, [2, 4]),            # Descending within digits
    (0, 9, [0, 2, 4, 6, 8]),   # Full digit range
    (10, 14, []),              # Range above single digits
    (100, 200, []),            # Large range
])
def test_standard_ranges(a, b, expected):
    """Tests standard functional requirements including directionality and digit constraints."""
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, []),                # Single odd digit
    (3, 3, []),                # Single odd digit
    (11, 11, []),              # Single non-digit
    (1, 3, [2]),               # Small range containing one even digit
    (7, 9, [8]),               # Small range containing one even digit
    (5, 7, [6]),               # Small range containing one even digit
])
def test_small_or_odd_ranges(a, b, expected):
    """Tests ranges that contain either no even digits or only one even digit."""
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (4, 4, [4]),               # Single even digit
    (0, 0, [0]),               # Zero as a single even digit
    (8, 9, [8]),               # Boundary: start is even
    (9, 8, [8]),               # Boundary: start is even (descending)
    (1, 2, [2]),               # Boundary: end is even
    (2, 1, [2]),               # Boundary: end is even (descending)
])
def test_boundary_and_single_even(a, b, expected):
    """Tests edge cases involving single even digits and range boundaries."""
    assert generate_integers(a, b) == expected

def test_all_even_digits_order():
    """Explicitly ensures the output is always in ascending order."""
    # Even if input is descending, output must be [0, 2, 4, 6, 8]
    assert generate_integers(8, 0) == [0, 2, 4, 6, 8]