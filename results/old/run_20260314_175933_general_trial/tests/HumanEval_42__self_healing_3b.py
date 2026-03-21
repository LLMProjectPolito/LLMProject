import pytest

def test_incr_list_empty():
    """Test incr_list with empty list."""
    assert incr_list([]) == []

def test_incr_list_single_element():
    """Test incr_list with single element."""
    assert incr_list([10]) == [11]

def test_incr_list_multiple_elements():
    """Test incr_list with multiple elements."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_incr_list_negative_numbers():
    """Test incr_list with negative numbers."""
    assert incr_list([-5, -3, -5, -2, -3, -3, -9, 0, 123]) == [-4, -2, -4, -1, -2, -2, -8, 1, 124]

def test_incr_list_non_integer_numbers():
    """Test incr_list with non-integer numbers."""
    with pytest.raises(TypeError):
        incr_list([1.5, 2.5, 3])

def test_incr_list_mixed_types():
    """Test incr_list with mixed types."""
    with pytest.raises(TypeError):
        incr_list([1, 2, '3'])

def test_incr_list_non_list_input():
    """Test incr_list with non-list input."""
    with pytest.raises(TypeError):
        incr_list('hello')

def test_incr_list_none_input():
    """Test incr_list with None input."""
    with pytest.raises(TypeError):
        incr_list(None)