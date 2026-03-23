import pytest
import math

def test_cycpattern_check_positive():
    assert cycpattern_check("abab", "baa") == True

def test_empty_string_b():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_wrong_type():
    """Test with non-string inputs."""
    assert cycpattern_check(123, "abc") == False
    assert cycpattern_check("abc", 456) == False
    assert cycpattern_check(None, "abc") == False
    assert cycpattern_check("abc", None) == False
    assert cycpattern_check(123, 456) == False