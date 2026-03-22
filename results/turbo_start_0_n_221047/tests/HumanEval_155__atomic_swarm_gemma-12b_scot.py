import pytest
import math

def test_even_odd_count_positive_mixed():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative_number():
    """Test with a negative number to ensure correct handling of the sign."""
    assert even_odd_count(-1234) == (2, 2)

import pytest

def test_even_odd_count_zero():
    """Test with zero input."""
    assert even_odd_count(0) == (1, 0)