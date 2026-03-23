import pytest
import math

def test_generate_integers_with_identical_negative_numbers():
    """Test case for identical negative numbers."""
    assert generate_integers(-2, -2) == []

def test_generate_integers_with_negative_input():
    """Test with negative input to ensure it handles it gracefully (returns empty list)."""
    assert generate_integers(-2, 2) == []