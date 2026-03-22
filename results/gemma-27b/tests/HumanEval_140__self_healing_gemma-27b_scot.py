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
    if "   " in text:
        text = text.replace("   ", "-")
        while "  " in text:
            text = text.replace("  ", "-")
        text = text.replace(" ", "_")
    else:
        text = text.replace(" ", "_")
    return text

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_trailing_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_two_consecutive_spaces():
    assert fix_spaces("Example  1") == "Example__1"

def test_three_consecutive_spaces():
    assert fix_spaces("Example   1") == "Example-1"

def test_more_than_three_consecutive_spaces():
    assert fix_spaces("Example    1") == "Example-1"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_only_spaces():
    assert fix_spaces("   ") == "-"

def test_string_with_only_two_spaces():
    assert fix_spaces("  ") == "__"

def test_string_with_leading_and_multiple_spaces():
    assert fix_spaces("   Example") == "-Example"

def test_string_with_multiple_spaces_and_trailing():
    assert fix_spaces("Example   ") == "Example-"