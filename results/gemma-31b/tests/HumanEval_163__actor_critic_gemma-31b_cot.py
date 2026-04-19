
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

def test_generate_integers_basic_ascending():
    """Test standard range where a < b and both are digits."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_basic_descending():
    """Test standard range where a > b and both are digits."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_out_of_digit_range():
    """Test range where both numbers are greater than 9."""
    assert generate_integers(10, 14) == []
    assert generate_integers(100, 200) == []

def test_generate_integers_partial_overlap_high():
    """Test range that starts within digits and ends above 9."""
    assert generate_integers(5, 15) == [6, 8]
    assert generate_integers(15, 5) == [6, 8]

def test_generate_integers_partial_overlap_low():
    """Test range that starts below 1 and ends within digits."""
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(5, 1) == [2, 4]

def test_generate_integers_single_even_digit():
    """Test range where a == b and the value is an even digit."""
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_odd_digit():
    """Test range where a == b and the value is an odd digit."""
    assert generate_integers(3, 3) == []

def test_generate_integers_single_non_digit():
    """Test range where a == b and the value is not a digit."""
    assert generate_integers(12, 12) == []

def test_generate_integers_full_digit_range():
    """Test range covering all possible digits. 0 is treated as a valid even digit."""
    assert generate_integers(0, 9) == [0, 2, 4, 6, 8]

def test_generate_integers_odd_boundaries():
    """Test range where boundaries are odd digits."""
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(7, 3) == [4, 6]

def test_generate_integers_large_numbers():
    """Test with very large positive integers."""
    assert generate_integers(10**6, 10**7) == []

def test_generate_integers_negative():
    """Test range including negative integers to verify digit filtering."""
    # Even digits in range [-2, 2] are 0 and 2
    assert generate_integers(-2, 2) == [0, 2]
    # No digits in range [-10, -5]
    assert generate_integers(-10, -5) == []

def test_generate_integers_floats():
    """Test range with floating point numbers to verify robustness."""
    # Even digits between 2.2 and 8.8 are 4, 6, 8
    assert generate_integers(2.2, 8.8) == [4, 6, 8]
    # Even digits between 2.0 and 8.0 are 2, 4, 6, 8
    assert generate_integers(2.0, 8.0) == [2, 4, 6, 8]