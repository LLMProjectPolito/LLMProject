import pytest
import math

def test_basic():
    assert cycpattern_check("hello","ell") == True

def test_empty_first_word():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_wrong_type():
    """Test with a non-string input."""
    try:
        cycpattern_check(123, "abc")
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass
    try:
        cycpattern_check("abc", 456)
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass