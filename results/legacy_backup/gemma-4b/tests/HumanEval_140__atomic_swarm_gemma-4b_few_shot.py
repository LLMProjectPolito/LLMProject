import pytest
import math

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"