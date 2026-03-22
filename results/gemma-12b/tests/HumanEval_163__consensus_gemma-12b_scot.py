import pytest

def test_generate_integers_ascending():
    """Test when a is less than b."""
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    """Test when a is greater than b."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    """Test when there are no even numbers between a and b."""
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    """Test when there is only one even number between a and b."""
    assert generate_integers(1, 3) == [2]

def test_generate_integers_same_number_even():
    """Test when a and b are the same even number."""
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_number_odd():
    """Test when a and b are the same odd number."""
    assert generate_integers(1, 1) == []

def test_generate_integers_negative_input():
    """Test with negative input (should still work as intended)."""
    assert generate_integers(-2, 4) == [-2, 0, 2, 4]

def test_generate_integers_zero_input():
    """Test with zero input."""
    assert generate_integers(0, 4) == [0, 2, 4]

def test_generate_integers_large_range():
    """Test with a large range of numbers."""
    assert generate_integers(1, 100) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]