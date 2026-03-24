import pytest

def test_generate_integers_ascending():
    """Test when a is less than b and both are even."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    """Test when a is greater than b and both are even."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    """Test when there are no even numbers between a and b."""
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    """Test when there is only one even number between a and b."""
    assert generate_integers(1, 3) == [2]

def test_generate_integers_a_is_even_b_is_odd():
    """Test when a is even and b is odd."""
    assert generate_integers(2, 5) == [2, 4]

def test_generate_integers_a_is_odd_b_is_even():
    """Test when a is odd and b is even."""
    assert generate_integers(3, 6) == [4, 6]

def test_generate_integers_a_equals_b_even():
    """Test when a and b are equal and even."""
    assert generate_integers(4, 4) == []

def test_generate_integers_a_equals_b_odd():
    """Test when a and b are equal and odd."""
    assert generate_integers(5, 5) == []

def test_generate_integers_negative_input():
    """Test with negative input (should still work as intended)."""
    assert generate_integers(-2, 2) == [-2, 0, 2]

def test_generate_integers_zero_input():
    """Test with zero input."""
    assert generate_integers(0, 4) == [0, 2, 4]