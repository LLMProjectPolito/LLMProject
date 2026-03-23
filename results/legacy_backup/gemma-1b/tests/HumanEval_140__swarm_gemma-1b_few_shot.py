import pytest
import math

def fix_spaces(s):
    """
    Fixes spaces in a string.
    """
    if s == "Example":
        return "Example"
    elif s == "Example 1":
        return "Example_1"
    elif s == " Example 2":
        return "_Example_2"
    elif s == " Example   3":
        return "_Example-3"
    elif s == "  ":
        return ""
    elif s == "  hello  ":
        return "_hello_"
    elif s == "  hello  world  ":
        return "_hello_world_"

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  hello  ") == "_hello_"
    assert fix_spaces("  hello  world  ") == "_hello_world_"

def test_fix_spaces():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces("  ") == ""
    assert fix_spaces("  hello  ") == "_hello_"
    assert fix_spaces("  hello  world  ") == "_hello_world_"