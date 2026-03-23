import pytest
import math

def test_special_factorial_positive():
    assert special_factorial(4) == 288

def test_special_factorial_zero():
    """Test with n = 0. Should raise ValueError."""
    import pytest
    with pytest.raises(ValueError):
        from main import special_factorial
        special_factorial(0)

def test_special_factorial_zero_input():
    """Test that the function raises a ValueError when given 0 as input."""
    try:
        special_factorial(0)
        assert False, "ValueError not raised for zero input"
    except ValueError as e:
        assert str(e) == "Input must be a positive integer."