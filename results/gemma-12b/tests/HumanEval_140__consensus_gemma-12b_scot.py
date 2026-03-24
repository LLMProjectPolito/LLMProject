
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

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_multiple_spaces_and_leading_space():
    assert fix_spaces("  Example   1 2") == "-Example-1_2"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_long_string_with_multiple_consecutive_spaces():
    assert fix_spaces("This is a very long string with   multiple    consecutive spaces.") == "This_is_a_very_long_string_with-multiple-consecutive_spaces."

def test_string_with_tabs_and_spaces():
    assert fix_spaces("Example\t1\t2") == "Example_1_2"

def test_string_with_newline_and_spaces():
    assert fix_spaces("Example\n1 2") == "Example_1_2"

def test_string_with_special_characters_and_spaces():
    assert fix_spaces("!@#$%^&*() Example   1") == "!@#$%^&*()_Example-3"

def test_string_with_numbers_and_spaces():
    assert fix_spaces("123 Example   456") == "123_Example-3"

def test_string_with_underscores_and_spaces():
    assert fix_spaces("Example_ 1   2") == "_Example_1-2"

def test_string_with_hyphens_and_spaces():
    assert fix_spaces("Example- 1   2") == "Example-1-2"