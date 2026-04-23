
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

import re
import pytest

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
    return re.sub(r" {3,}", "-", text).replace(" ", "_")

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_no_spaces():
    assert fix_spaces("NoSpaces") == "NoSpaces"

def test_fix_spaces_leading_and_trailing():
    assert fix_spaces("  Leading and Trailing  ") == "__Leading_and_Trailing__"

def test_fix_spaces_many_spaces():
    assert fix_spaces("Multiple   Consecutive   Spaces") == "Multiple-Consecutive-Spaces"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("Mixed  Spaces  Here") == "Mixed-Spaces_Here"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_two_consecutive_spaces():
    assert fix_spaces("Two  Spaces") == "Two_Spaces"

def test_fix_spaces_tabs_only():
    assert fix_spaces("\t\t\t") == "\t\t\t"

def test_fix_spaces_newlines():
    assert fix_spaces("Line1\nLine2") == "Line1\nLine2"

def test_fix_spaces_order_of_operations():
    assert fix_spaces("Two  Spaces   More") == "Two_Spaces-More"

def test_fix_spaces_multiple_occurrences():
    assert fix_spaces("A   B  C    D") == "A-B_C-D"

def test_fix_spaces_tabs_and_multiple_spaces():
    assert fix_spaces("Tab\t\t and   Spaces") == "Tab_and-Spaces"