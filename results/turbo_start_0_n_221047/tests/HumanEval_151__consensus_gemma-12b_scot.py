import pytest

def test_empty_list():
    """Test with an empty list."""
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    """Test with a list of positive odd numbers."""
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_mixed_positive_and_even_numbers():
    """Test with a list of positive odd, even, and zero numbers."""
    assert double_the_difference([1, 2, 3, 4, 0]) == 1 + 9

def test_negative_numbers():
    """Test with a list containing negative numbers."""
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive_numbers():
    """Test with a list containing both negative and positive numbers."""
    assert double_the_difference([-1, 2, 3, -4, 5]) == 9 + 25

def test_zero_only():
    """Test with a list containing only zero."""
    assert double_the_difference([0]) == 0

def test_single_odd_number():
    """Test with a list containing a single odd number."""
    assert double_the_difference([7]) == 49

def test_single_even_number():
    """Test with a list containing a single even number."""
    assert double_the_difference([4]) == 0

def test_mixed_types():
    """Test with a list containing mixed types (should ignore non-integers)."""
    assert double_the_difference([1, 2.5, "a", 3]) == 1 + 9

def test_large_numbers():
    """Test with large odd numbers."""
    assert double_the_difference([101, 303]) == 10201 + 91809

def test_all_even_numbers():
    """Test with a list containing only even numbers."""
    assert double_the_difference([2, 4, 6, 8]) == 0