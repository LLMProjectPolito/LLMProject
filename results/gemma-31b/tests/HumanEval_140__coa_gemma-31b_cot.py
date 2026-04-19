
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """

import pytest
import math


# Focus: Boundary Values
def test_fix_spaces_boundary_two_spaces():
    # Boundary: Exactly 2 spaces (should be underscores, as it's not > 2)
    assert fix_spaces("a  b") == "a__b"

def test_fix_spaces_boundary_three_spaces():
    # Boundary: Exactly 3 spaces (should be hyphen, as it is > 2)
    assert fix_spaces("a   b") == "a-b"

def test_fix_spaces_boundary_empty():
    # Boundary: Empty string
    assert fix_spaces("") == ""

# Focus: Logic Branches
import pytest

def test_fix_spaces_underscores():
    # Branch: 1 or 2 consecutive spaces should be replaced by underscores
    assert fix_spaces("Hello World") == "Hello_World"
    assert fix_spaces("Hello  World") == "Hello__World"
    assert fix_spaces("  ") == "__"

def test_fix_spaces_hyphens():
    # Branch: More than 2 consecutive spaces should be replaced by a single hyphen
    assert fix_spaces("Hello   World") == "Hello-World"
    assert fix_spaces("Hello    World") == "Hello-World"
    assert fix_spaces("   ") == "-"

def test_fix_spaces_mixed_branches():
    # Branch: Mixed cases of single/double and triple+ spaces
    assert fix_spaces(" a  b   c    d ") == "_a__b-c-d_"

# Focus: Edge Cases
import pytest

def test_fix_spaces_empty_and_no_spaces():
    assert fix_spaces("") == ""
    assert fix_spaces("NoSpaces") == "NoSpaces"

def test_fix_spaces_boundary_consecutive():
    # Exactly 2 spaces should be underscores (not more than 2)
    assert fix_spaces("  ") == "__"
    # 3 spaces should be a hyphen
    assert fix_spaces("   ") == "-"
    # 4 spaces should be a hyphen
    assert fix_spaces("    ") == "-"

def test_fix_spaces_extreme_positions():
    # Spaces at start, end, and mixed lengths
    assert fix_spaces("  start and end  ") == "__start_and_end__"
    assert fix_spaces("   leading and trailing   ") == "-leading_and_trailing-"