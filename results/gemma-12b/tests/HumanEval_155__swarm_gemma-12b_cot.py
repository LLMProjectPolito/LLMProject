import pytest
import math

def test_even_odd_count_zero():
    """Test case for input 0."""
    assert even_odd_count(0) == (1, 0)