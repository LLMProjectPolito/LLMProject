
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
def test_fix_spaces_boundary_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_boundary_two_spaces():
    # Exactly 2 spaces: not "more than 2", so should be replaced by underscores
    assert fix_spaces("  ") == "__"

def test_fix_spaces_boundary_three_spaces():
    # Exactly 3 spaces: "more than 2", so should be replaced by a single hyphen
    assert fix_spaces("   ") == "-"

# Focus: Type Scenarios
import pytest

def test_fix_spaces_none():
    with pytest.raises(TypeError):
        fix_spaces(None)

def test_fix_spaces_int():
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_list():
    with pytest.raises(TypeError):
        fix_spaces(["Example 1"])

# Focus: Logic Branches
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_or_double_spaces():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces("Example  1") == "Example__1"

def test_fix_spaces_more_than_two_spaces():
    assert fix_spaces("Example   1") == "Example-1"
    assert fix_spaces("Example    1") == "Example-1"
    assert fix_spaces(" Example   3") == "_Example-3"