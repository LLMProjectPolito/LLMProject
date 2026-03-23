import pytest
import math

def test_fix_spaces_basic():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_consecutive():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_multiple_consecutive():
    assert fix_spaces("  Example   Test  ") == "_Example-Test_"