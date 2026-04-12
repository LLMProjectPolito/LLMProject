
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

def test_fix_spaces_two_consecutive():
    # Boundary: 2 spaces is not "more than 2", should be replaced by underscores
    assert fix_spaces("  ") == "__"

def test_fix_spaces_three_consecutive():
    # Boundary: 3 spaces is "more than 2", should be replaced by a hyphen
    assert fix_spaces("   ") == "-"

# Focus: Logic Branches
def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_standard_underscores():
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces("Example  2") == "Example__2"

def test_fix_spaces_consecutive_hyphen():
    assert fix_spaces("Example   3") == "Example-3"
    assert fix_spaces("Example    4") == "Example-4"

# Focus: Edge Cases
def test_fix_spaces_boundary_counts():
    assert fix_spaces("") == ""
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"

def test_fix_spaces_positional_edges():
    assert fix_spaces("   leading") == "-leading"
    assert fix_spaces("trailing   ") == "trailing-"
    assert fix_spaces("  both  ") == "__both__"
    assert fix_spaces("   both   ") == "-both-"

def test_fix_spaces_only_spaces():
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("     ") == "-"