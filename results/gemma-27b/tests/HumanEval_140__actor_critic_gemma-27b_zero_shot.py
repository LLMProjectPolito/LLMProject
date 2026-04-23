
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
    text = text.replace("   ", "-")
    text = text.replace(" ", "_")
    return text

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_trailing_space():
    assert fix_spaces("Example 1 ") == "Example_1_"

def test_leading_trailing():
    assert fix_spaces(" Example 1 ") == "_Example_1_"

def test_multiple_spaces_with_leading_trailing():
    assert fix_spaces("  Example   1  ") == "_Example-1_"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_string_with_many_spaces():
    assert fix_spaces("   Example     1        2   ") == "-Example---------1---------2-"

def test_consecutive_spaces_at_start():
    assert fix_spaces("   Example") == "-Example"

def test_consecutive_spaces_in_middle():
    assert fix_spaces("Example   Middle") == "Example-Middle"

def test_four_consecutive_spaces():
    assert fix_spaces("Example    5") == "Example-5"

def test_five_consecutive_spaces():
    assert fix_spaces("Example     6") == "Example-6"

def test_leading_and_multiple_spaces():
    assert fix_spaces("   Example  7") == "-Example__7"

def test_multiple_spaces_and_trailing():
    assert fix_spaces("Example   8 ") == "Example-8_"