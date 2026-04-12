
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
def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_two_spaces_boundary():
    # Exactly 2 spaces should be replaced by underscores as it is not "more than 2"
    assert fix_spaces("  ") == "__"

def test_fix_spaces_three_spaces_boundary():
    # Exactly 3 spaces is the first instance of "more than 2"
    assert fix_spaces("   ") == "-"

# Focus: Logic Branches
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_double():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces("Example  2") == "Example__2"

def test_fix_spaces_more_than_two():
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("Example    4") == "Example-4"

# Focus: Edge Cases
def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_exactly_two_spaces():
    assert fix_spaces("  ") == "__"

def test_fix_spaces_only_many_spaces():
    assert fix_spaces("    ") == "-"