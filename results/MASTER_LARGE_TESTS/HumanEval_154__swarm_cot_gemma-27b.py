import pytest

def test_cycpattern_check_empty_b():
    """Test case for when the second word (b) is empty."""
    assert cycpattern_check("abcd", "") == True