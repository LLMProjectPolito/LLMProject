import pytest
import math

def test_even_odd_count_positive():
    assert even_odd_count(123456) == (3, 3)

def test_even_odd_count_zero():
    """Test with zero input."""
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_invalid_input():
    """Test with a float input to ensure it handles non-integer input gracefully."""
    import pytest
    with pytest.raises(TypeError):
        even_odd_count(1.5)