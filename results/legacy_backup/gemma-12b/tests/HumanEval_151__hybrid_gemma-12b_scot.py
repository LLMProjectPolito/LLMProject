import pytest
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    """Test with an empty list."""
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    """Test with a list containing only even numbers."""
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_only_odd_numbers():
    """Test with a list containing only odd numbers."""
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49

def test_mixed_odd_and_even():
    """Test with a mix of odd and even numbers."""
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25

def test_negative_numbers():
    """Test with negative numbers."""
    assert double_the_difference([-1, -2, -3]) == 0

def test_non_integer_numbers():
    """Test with non-integer numbers (floats)."""
    assert double_the_difference([1.5, 2.0, 3.7]) == 0

def test_mixed_valid_and_invalid():
    """Test with a mix of valid and invalid numbers."""
    assert double_the_difference([1, -2, 3.5, 5, -7]) == 1 + 25

def test_zero_in_list():
    """Test with zero in the list."""
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_large_numbers():
    """Test with large odd numbers."""
    assert double_the_difference([1001, 1003]) == 1001**2 + 1003**2

def test_single_odd_number():
    """Test with a single odd number."""
    assert double_the_difference([7]) == 49

def test_single_even_number():
    """Test with a single even number."""
    assert double_the_difference([2]) == 0

def test_only_negative_numbers():
    """Test with only negative numbers."""
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_numbers():
    """Test with mixed positive, negative, and zero."""
    assert double_the_difference([1, 2, 3, -4, 5, 0]) == 1 + 9 + 25