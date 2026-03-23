import pytest

def test_empty_list():
    """Test case for an empty list."""
    result = sum_squares([])
    assert result == 0

def test_list_with_no_multiples():
    """Test case for a list with no multiples of 3 or 4."""
    result = sum_squares([1, 2, 4, 5, 7])
    assert result == 19

def test_list_with_multiples_of_3():
    """Test case for a list with multiples of 3."""
    result = sum_squares([1, 2, 3, 4, 5, 6])
    assert result == 42

def test_list_with_multiples_of_4():
    """Test case for a list with multiples of 4."""
    result = sum_squares([1, 2, 3, 4, 5, 6, 7, 8])
    assert result == 106

def test_list_with_multiples_of_3_and_4():
    """Test case for a list with multiples of both 3 and 4."""
    result = sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12])
    assert result == 186

def test_list_with_negative_numbers():
    """Test case for a list with negative numbers."""
    result = sum_squares([-1, -2, -3, -4, -5])
    assert result == -126

def test_list_with_mixed_positive_and_negative():
    """Test case for a list with mixed positive and negative numbers."""
    result = sum_squares([-1, 2, -3, 4, -5, 6])
    assert result == 46

def test_list_with_zeros():
    """Test case for a list with zeros."""
    result = sum_squares([0, 1, 2, 3, 4, 5])
    assert result == 55

def test_list_with_large_numbers():
    """Test case for a list with large numbers."""
    result = sum_squares([100, 200, 300, 400])
    assert result == 300000

def test_list_with_duplicate_numbers():
    """Test case for a list with duplicate numbers."""
    result = sum_squares([1, 1, 1, 1, 1])
    assert result == 5