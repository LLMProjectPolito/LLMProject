import pytest
import math

def test_fix_spaces_basic():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_consecutive():
    assert fix_spaces("  hello   world  ") == "--hello---world--"

def test_fix_spaces_consecutive():
    assert fix_spaces("hello   world") == "hello-world"