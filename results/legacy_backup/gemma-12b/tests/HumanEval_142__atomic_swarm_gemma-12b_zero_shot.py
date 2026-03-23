import pytest
import math

def test_basic():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 180

def test_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_wrong_type():
    """Test with a list containing a non-integer."""
    import pytest
    with pytest.raises(TypeError):
        sum_squares([1, 2, "a"])