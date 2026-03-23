import pytest
import math

def test_basic():
    assert sum_squares([1, 2, 3]) == 14

def test_empty_list():
    """Test with an empty list."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([]) == 0

def test_sum_squares_invalid_input():
    """Test with a list containing a non-integer element."""
    import pytest
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])