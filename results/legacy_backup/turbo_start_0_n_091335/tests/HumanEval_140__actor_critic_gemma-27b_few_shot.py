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

def test_fix_spaces_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_fix_spaces_trailing_space():
    assert fix_spaces("Example 4 ") == "Example_4_"

def test_fix_spaces_leading_and_trailing_spaces():
    assert fix_spaces(" Example 5 ") == "_Example_5_"

def test_fix_spaces_multiple_consecutive_spaces():
    assert fix_spaces("Example    6") == "Example-6"

def test_fix_spaces_leading_multiple_spaces():
    assert fix_spaces("   Example 7") == "-Example_7"

def test_fix_spaces_trailing_multiple_spaces():
    assert fix_spaces("Example 8   ") == "Example_8-"

def test_fix_spaces_only_spaces_three():
    assert fix_spaces("   ") == "-"

def test_fix_spaces_only_spaces_four():
    assert fix_spaces("    ") == "-"

def test_fix_spaces_only_spaces_five():
    assert fix_spaces("     ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  Example   9  ") == "_-Example-9_"
    assert fix_spaces("   Example  10   ") == "-Example_10-"

def test_fix_spaces_empty_string():
    assert fix_spaces("") == ""

def test_fix_spaces_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1" # Function only handles spaces.