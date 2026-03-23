import pytest
import math

def test_special_factorial_positive():
    assert special_factorial(4) == 288

def test_special_factorial_zero():
    """Test with n = 0, which should return 1."""
    assert special_factorial(0) == 1

def test_special_factorial_zero():
    """Test that special_factorial(0) raises a ValueError."""
    import pytest
    with pytest.raises(ValueError):
        special_factorial(0)