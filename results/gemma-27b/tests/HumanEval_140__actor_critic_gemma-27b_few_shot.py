
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
    return text.replace("   ", "-").replace(" ", "_")

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 1 ") == "Example_1_"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces(" Example 1 ") == "_Example_1_"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("Example    4") == "Example-4"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Example   5  ") == "-Example-5-"

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_focused_mixed_spaces():
    assert fix_spaces("a  b   c") == "a-b-c"

def test_fix_spaces_more_than_three_spaces():
    assert fix_spaces("a    b") == "a-b"

def test_fix_spaces_exactly_two_spaces():
    assert fix_spaces("a  b") == "a_b"