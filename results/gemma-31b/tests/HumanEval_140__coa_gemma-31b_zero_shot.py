
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
def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_two_spaces():
    assert fix_spaces("  ") == "__"

def test_fix_spaces_three_spaces():
    assert fix_spaces("   ") == "-"

# Focus: Logic Branches
import pytest

def test_fix_spaces_underscore_branch():
    # Tests the branch where spaces are replaced by underscores (1 or 2 spaces)
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces("Example  2") == "Example__2"
    assert fix_spaces(" Example ") == "_Example_"

def test_fix_spaces_hyphen_branch():
    # Tests the branch where more than 2 consecutive spaces are replaced by a hyphen
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("Example    4") == "Example-4"
    assert fix_spaces("   Example") == "-Example"

# Focus: Type Scenarios
import pytest

def test_fix_spaces_none_type():
    with pytest.raises(TypeError):
        fix_spaces(None)

def test_fix_spaces_int_type():
    with pytest.raises(TypeError):
        fix_spaces(123)

def test_fix_spaces_list_type():
    with pytest.raises(TypeError):
        fix_spaces(["Example 1"])