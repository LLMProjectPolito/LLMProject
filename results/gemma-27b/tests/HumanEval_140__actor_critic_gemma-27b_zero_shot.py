
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
    if "___" in text:
        return text.replace("___", "-")
    else:
        return text

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_trailing_space():
    assert fix_spaces("Example 1 ") == "Example_1_"

def test_leading_trailing_spaces():
    assert fix_spaces(" Example 1 ") == "_Example_1_"

def test_multiple_spaces_with_leading_and_trailing():
    assert fix_spaces("  Example   1  ") == "__Example-1__"

def test_only_spaces():
    assert fix_spaces("   ") == "___"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_string_with_many_spaces():
    assert fix_spaces("   Example     1      2   ") == "___Example------1------2___"

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_carriage_returns():
    assert fix_spaces("Example\r1") == "Example_1"

def test_two_spaces_then_single():
    assert fix_spaces("Example  1") == "Example__1"

def test_consecutive_four_spaces():
    assert fix_spaces("Example    1") == "Example-1"

def test_consecutive_spaces_at_beginning():
    assert fix_spaces("   Example 1") == "___Example_1"

def test_vertical_tab():
    assert fix_spaces("Example\v1") == "Example_1"

def test_form_feed():
    assert fix_spaces("Example\f1") == "Example_1"