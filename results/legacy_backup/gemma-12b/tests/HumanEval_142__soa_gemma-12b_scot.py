import pytest

def test_empty_list():
    """Test case for an empty list."""
    result = sum_squares([])
    assert result == 0

def test_list_with_no_multiples():
    """Test case for a list with no multiples of 3 or 4."""
    lst = [1, 2, 3, 4, 5]
    expected = sum(lst)
    result = sum_squares(lst)
    assert result == expected

def test_list_with_multiples_of_3():
    """Test case for a list with multiples of 3."""
    lst = [1, 2, 3, 4, 5, 6]
    expected = 1 + 2 + (3**2) + 4 + 5 + (6**2)
    result = sum_squares(lst)
    assert result == expected

def test_list_with_multiples_of_4():
    """Test case for a list with multiples of 4."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = 1 + 2 + 3 + (4**3) + 5 + 6 + 7 + (8**3)
    result = sum_squares(lst)
    assert result == expected

def test_list_with_multiples_of_3_and_4():
    """Test case for a list with multiples of both 3 and 4."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1 + 2 + (3**2) + (4**3) + 5 + 6 + 7 + (8**3) + 9 + 10 + 11 + (12**2)
    result = sum_squares(lst)
    assert result == expected

def test_list_with_negative_numbers():
    """Test case for a list with negative numbers."""
    lst = [-1, -2, -3, -4, -5]
    expected = (-1) + (-2) + ((-3)**2) + ((-4)**3) + (-5)
    result = sum_squares(lst)
    assert result == expected

def test_list_with_mixed_positive_and_negative_numbers():
    """Test case for a list with mixed positive and negative numbers."""
    lst = [-1, -5, 2, -1, -5]
    expected = (-1) + (-5**2) + 2 + (-1) + (-5**3)
    result = sum_squares(lst)
    assert result == -126

def test_list_with_zeros():
    """Test case for a list with zeros."""
    lst = [0, 1, 2, 3, 4]
    expected = 0 + 1 + 2 + (3**2) + (4**3)
    result = sum_squares(lst)
    assert result == 77