import pytest
import math

def test_cycpattern_check_positive():
    assert cycpattern_check("abab", "baa") == True

def test_empty_first_word():
    """Test case: First word is empty."""
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_wrong_type():
    """Test with non-string inputs."""
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

    try:
        cycpattern_check(123, 456)
        assert False, "Should have raised a TypeError"
    except TypeError:
        pass