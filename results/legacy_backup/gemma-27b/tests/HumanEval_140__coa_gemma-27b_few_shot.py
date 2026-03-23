import pytest
import math


# Focus: Boundary Values
def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_fix_spaces_many_spaces():
    assert fix_spaces("   Example      3   ") == "-Example-3-"

# Focus: Consecutive Spaces
def test_fix_spaces_no_consecutive():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_two_consecutive():
    assert fix_spaces("Example  2") == "Example__2"

def test_fix_spaces_more_than_two_consecutive():
    assert fix_spaces("Example   3") == "Example-3"

# Focus: Leading/Trailing Spaces
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_trailing_single():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_leading_trailing_multiple():
    assert fix_spaces("   Example   ") == "-Example-"