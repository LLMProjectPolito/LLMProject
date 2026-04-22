
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
    text = text.replace(" ", "_")
    while "   " in text:
        text = text.replace("   ", "-")
    return text

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example ") == "Example_ "

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_trailing_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_complex_case():
    assert fix_spaces("  This   is   a   test  ") == "_This--is--a--test_"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "___"

def test_fix_spaces_mixed_spaces_and_other_chars():
    assert fix_spaces("a b c   d") == "a_b_c--d"