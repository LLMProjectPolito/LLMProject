
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    low, high = min(a, b), max(a, b)
    return [d for d in [0, 2, 4, 6, 8] if low <= d <= high]

import pytest

def test_generate_integers_basic():
    """Test basic range of even digits."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    """Test that the function handles inputs regardless of order."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_out_of_digit_range():
    """Test that integers greater than 9 return an empty list as they aren't digits."""
    assert generate_integers(10, 14) == []

def test_generate_integers_mixed_range():
    """Test range containing both even and odd digits."""
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_single_digit_even():
    """Test range where a and b are the same even digit."""
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_digit_odd():
    """Test range where a and b are the same odd digit."""
    assert generate_integers(3, 3) == []

def test_generate_integers_full_digit_span():
    """Test range covering all possible digits."""
    assert generate_integers(1, 9) == [2, 4, 6, 8]

def test_generate_integers_large_bounds():
    """Test bounds that extend beyond the digit range."""
    # Only digits (0-9) that are even and within [1, 100] are [2, 4, 6, 8]
    assert generate_integers(1, 100) == [2, 4, 6, 8]
    assert generate_integers(100, 1) == [2, 4, 6, 8]

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (1, 1, []),
    (2, 2, [2]),
    (1, 3, [2]),
    (0, 2, [0, 2]), # Including 0 if the implementation treats it as a non-negative digit
    (5, 5, []),
])
def test_generate_integers_parametrized(a, b, expected):
    """Parametrized tests for various edge cases."""
    assert generate_integers(a, b) == expected