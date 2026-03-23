import pytest
import math

def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_edge_n_is_zero():
    """Test when n is zero (not a prime)."""
    assert x_or_y(0, 34, 12) == 12

def test_x_or_y_invalid_input():
    """Tests the function with a non-integer input for n."""
    import pytest
    with pytest.raises(TypeError):
        x_or_y("abc", 1, 2)