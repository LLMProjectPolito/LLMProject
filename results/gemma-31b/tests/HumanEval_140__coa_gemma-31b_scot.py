
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
    # Exactly 2 spaces: not "more than 2", so should be underscores
    assert fix_spaces("  ") == "__"

def test_fix_spaces_three_spaces_boundary():
    # Exactly 3 spaces: "more than 2", so should be a single dash
    assert fix_spaces("   ") == "-"

# Focus: Logic Branches
import pytest

def test_fix_spaces_single_or_double():
    # Tests the branch where spaces are present but not more than 2 consecutively
    assert fix_spaces("Hello World") == "Hello_World"
    assert fix_spaces("Hello  World") == "Hello__World"
    assert fix_spaces("NoSpaces") == "NoSpaces"

def test_fix_spaces_more_than_two():
    # Tests the branch where 3 or more consecutive spaces are replaced by a hyphen
    assert fix_spaces("Hello   World") == "Hello-World"
    assert fix_spaces("Hello    World") == "Hello-World"
    assert fix_spaces("   Leading") == "-Leading"

def test_fix_spaces_mixed_branches():
    # Tests a combination of both logic branches in one string
    assert fix_spaces(" a  b   c ") == "_a__b-c_"

# Focus: Edge Cases
def test_fix_spaces_empty_and_boundary():
    assert fix_spaces("") == ""
    assert fix_spaces("  ") == "__"  # Exactly 2 spaces is not "more than 2"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"
    assert fix_spaces("     ") == "-"

def test_fix_spaces_mixed_edge_cases():
    assert fix_spaces("  a   b  ") == "__a-b__"
    assert fix_spaces("   ") == "-"