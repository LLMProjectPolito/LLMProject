import pytest
import math

def test_fix_spaces_typical():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""