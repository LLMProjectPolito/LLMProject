
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
from your_module import fix_spaces  # Replace your_module

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_consecutive_spaces():
    assert fix_spaces("Example   3") == "Example-3"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_leading_and_trailing_spaces():
    assert fix_spaces("  Example 2  ") == "-Example_2-"

def test_mixed_spaces():
    assert fix_spaces("Example 1  2   3") == "Example_1-2-3"

def test_numbers_only():
    assert fix_spaces("1 2 3") == "1_2_3"

def test_special_characters():
    assert fix_spaces("!@# $ %") == "!@#_$ %"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_long_consecutive_spaces():
    assert fix_spaces("Example     3") == "Example-3"

def test_newline_characters():
    assert fix_spaces("Example\n1") == "Example_1"

def test_tab_characters():
    assert fix_spaces("Example\t1") == "Example_1"

def test_mixed_characters_and_spaces():
    assert fix_spaces("  Hello 123 World!  ") == "-Hello_123_World!-"