import pytest
import math

def test_sum_squares_positive():
    """Test with a list containing elements at multiples of 3 and 4."""
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1**2 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9 + 10**2 + 11 + 12**3
    assert sum_squares(lst) == expected

def test_empty_list():
    """Test with an empty list to ensure it returns 0."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([]) == 0

def test_sum_squares_wrong_type():
    """Test with a list containing a non-integer element."""
    import pytest
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])