import pytest
import math

def test_basic():
    assert cycpattern_check("abcd","abd") == False

def test_empty_string():
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "") == True

import pytest

def test_empty_string():
    assert cycpattern_check("", "a") == False
    assert cycpattern_check("abc", "") == True
    assert cycpattern_check("", "") == True