
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
        return text.replace("   ", "-").replace(" ", "_")
    else:
        return text.replace(" ", "_")

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

def test_multiple_with_leading_trailing():
    assert fix_spaces("  Example   1  ") == "_Example-1_"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_string_with_many_spaces():
    assert fix_spaces("   Example     1        2   ") == "-Example---------1---------2-"

def test_string_with_four_spaces():
    assert fix_spaces("Example    3") == "Example-3"

def test_leading_trailing_multiple_spaces():
    assert fix_spaces("   Example   ") == "-Example-"

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example\t1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example\n1"

def test_leading_trailing_and_multiple():
    assert fix_spaces("  Example  1   2  ") == "_Example__1-2_"