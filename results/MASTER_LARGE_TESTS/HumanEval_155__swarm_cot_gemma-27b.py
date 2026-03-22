import pytest

def test_even_odd_count_negative_number_with_zero():
    """Test case for a negative number containing zero."""
    assert even_odd_count(-120) == (2, 1)
    assert even_odd_count(-102) == (2, 1)