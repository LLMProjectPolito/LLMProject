import pytest

def test_special_factorial_zero():
    """Test the edge case where n is 0. Should raise ValueError."""
    with pytest.raises(ValueError):
        special_factorial(0)