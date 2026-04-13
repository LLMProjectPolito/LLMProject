
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
    # Boundary: exactly 2 spaces should be underscores, not a dash
    assert fix_spaces("  ") == "__"
    assert fix_spaces("a  b") == "a__b"

def test_fix_spaces_boundary_three_spaces():
    # Boundary: 3 or more spaces should be replaced by a single dash
    assert fix_spaces("   ") == "-"
    assert fix_spaces("a   b") == "a-b"
    assert fix_spaces("a    b") == "a-b"

def test_fix_spaces_boundary_empty():
    # Boundary: empty string
    assert fix_spaces("") == ""

# Focus: Logic Branches
def test_fix_spaces_single_double_branches():
    # Branch: 1 or 2 consecutive spaces should be replaced by underscores
    assert fix_spaces("Hello World") == "Hello_World"
    assert fix_spaces("Hello  World") == "Hello__World"

def test_fix_spaces_triple_plus_branches():
    # Branch: More than 2 consecutive spaces should be replaced by a single hyphen
    assert fix_spaces("Hello   World") == "Hello-World"
    assert fix_spaces("Hello    World") == "Hello-World"

def test_fix_spaces_mixed_branches():
    # Branch: Mixed occurrences of single/double and triple+ spaces
    assert fix_spaces(" a  b   c    d") == "_a__b-c-d"

# Focus: Type Scenarios
import pytest

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_none_type():
    with pytest.raises(TypeError):
        fix_spaces(None)

def test_fix_spaces_numeric_type():
    with pytest.raises(TypeError):
        fix_spaces(123)