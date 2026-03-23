import pytest

def test_negative_number_with_zero():
    """Test case for a negative number containing zero."""
    assert even_odd_count(-102) == (2, 1)