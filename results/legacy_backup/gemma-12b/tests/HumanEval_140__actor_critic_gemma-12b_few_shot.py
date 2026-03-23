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
    text = re.sub(r"\s{2,}", "-", text)
    text = text.replace(" ", "_")
    return text

import pytest

def test_fix_spaces_basic():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_only_spaces():
    assert fix_spaces("   ") == "---"

def test_fix_spaces_multiple_consecutive_groups():
    assert fix_spaces("  Example   1   ") == "-Example-1-"

def test_fix_spaces_trailing_spaces():
    assert fix_spaces("Example   ") == "Example---"

def test_fix_spaces_mixed_spaces_and_underscores():
    assert fix_spaces("Example_with_underscores  1") == "Example_with_underscores_1"

def test_fix_spaces_leading_multiple_spaces():
    assert fix_spaces("   Example") == "---Example"

def test_fix_spaces_trailing_multiple_spaces():
    assert fix_spaces("Example   ") == "Example---"