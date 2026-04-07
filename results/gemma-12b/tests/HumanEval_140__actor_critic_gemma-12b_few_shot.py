
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
    new_text = text.replace(" ", "_")
    new_text = re.sub(r"_{3,}", "-", new_text)
    return new_text

import pytest

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("Example   ") == "Example-"

def test_fix_spaces_mixed():
    assert fix_spaces("  Example   Test  ") == "-Example-Test-"

def test_fix_spaces_two_consecutive():
    assert fix_spaces("Example  Test") == "Example__Test"

def test_fix_spaces_three_consecutive():
    assert fix_spaces("Example   Test") == "Example-Test"

def test_fix_spaces_four_consecutive():
    assert fix_spaces("Example    Test") == "Example-Test"

def test_fix_spaces_five_consecutive():
    assert fix_spaces("Example     Test") == "Example-Test"