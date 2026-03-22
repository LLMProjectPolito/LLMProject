import pytest

def test_special_factorial_zero():
    """Test with n = 0, which should raise a ValueError."""
    with pytest.raises(ValueError):
        special_factorial(0)