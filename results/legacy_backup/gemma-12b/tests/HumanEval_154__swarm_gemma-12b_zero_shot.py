import pytest
import math

def test_cycpattern_check_empty_pattern():
    assert cycpattern_check("anyword", "") == True
    assert cycpattern_check("anytext", "") == True
    assert cycpattern_check("anyword", "") == True