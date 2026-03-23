import pytest
import math

def test_special_factorial_zero_raises_value_error():
    """Test with n = 0. Should raise a ValueError."""
    with pytest.raises(ValueError):
        from main import special_factorial
        special_factorial(0)

def test_special_factorial_zero_returns_one():
    """Test with n = 0. The loop should not execute, and the initial value 1 should be returned."""
    assert special_factorial(0) == 1