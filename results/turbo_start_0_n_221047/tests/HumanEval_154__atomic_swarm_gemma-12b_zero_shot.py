import pytest
import math

def test_basic():
    assert cycpattern_check("hello","ell") == True

def test_empty_first_word():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_wrong_type():
    """Test with non-string inputs."""
    assert cycpattern_check(123, "abc") == False
    assert cycpattern_check("abc", 456) == False
    assert cycpattern_check(123, 456) == False