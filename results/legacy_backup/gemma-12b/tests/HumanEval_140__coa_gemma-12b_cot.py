import pytest
import math


# Focus: Boundary Values
import pytest

def test_fix_spaces_leading_trailing_spaces():
    assert fix_spaces("  Example") == "__Example"
    assert fix_spaces("Example  ") == "Example__"
    assert fix_spaces("  Example  ") == "__Example__"

def test_fix_spaces_consecutive_spaces_at_start():
    assert fix_spaces("   Example") == "---Example"
    assert fix_spaces("    Example") == "----Example"

def test_fix_spaces_consecutive_spaces_at_end():
    assert fix_spaces("Example   ") == "Example---"
    assert fix_spaces("Example    ") == "Example----"

# Focus: Logic Branches
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

# Focus: Type Scenarios
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"