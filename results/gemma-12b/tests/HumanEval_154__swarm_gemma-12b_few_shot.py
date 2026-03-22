import pytest
import math

def test_cycpattern_check_rotation_at_end():
    assert cycpattern_check("abcde", "eabc") == True

def test_cycpattern_check_rotation_at_end_2():
    assert cycpattern_check("abab", "ba") == True

def test_cycpattern_check_rotation_at_end_3():
    assert cycpattern_check("abab", "ba") == True