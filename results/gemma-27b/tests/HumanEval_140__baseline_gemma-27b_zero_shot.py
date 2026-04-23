
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
    if "   " in text:
        return text.replace("   ", "-")
    else:
        return text.replace(" ", "_")

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_trailing_space():
    assert fix_spaces("Example 1 ") == "Example_1_"

def test_multiple_leading_and_trailing_spaces():
    assert fix_spaces("  Example  ") == "_Example_"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example-1-2"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example\t1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example\n1"

def test_long_string_with_multiple_spaces():
    long_string = "This is a very long string with   multiple   spaces and some  single spaces."
    expected_string = "This_is_a_very_long_string_with-multiple-spaces_and_some_single_spaces."
    assert fix_spaces(long_string) == expected_string