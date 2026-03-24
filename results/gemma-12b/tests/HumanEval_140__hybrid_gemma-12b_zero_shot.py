
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

def test_multiple_consecutive_spaces_at_beginning():
    assert fix_spaces("   Example 4") == "-Example_4"

def test_multiple_consecutive_spaces_at_end():
    assert fix_spaces("Example 5   ") == "Example_5-"

def test_multiple_consecutive_spaces_in_middle():
    assert fix_spaces("Example  6  7") == "Example_6-7"

def test_mixed_spaces():
    assert fix_spaces("Example  8   9  10") == "Example_8-9_10"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_long_string_with_consecutive_spaces():
    assert fix_spaces("This is a very long string with   multiple    consecutive spaces.") == "This_is_a_very_long_string_with-multiple-consecutive_spaces."

def test_string_with_tabs_and_spaces():
    assert fix_spaces("Example\t 1") == "Example_1"

def test_string_with_newlines_and_spaces():
    assert fix_spaces("Example\n 1") == "Example_1"

def test_string_with_special_characters_and_spaces():
    assert fix_spaces("!@#$%^&*() Example  1") == "!@#$%^&*()_Example-1"

def test_string_with_numbers_and_spaces():
    assert fix_spaces("123 Example   456") == "123_Example-456"

def test_string_with_mixed_characters_and_spaces():
    assert fix_spaces("a b  c   d") == "a_b-c_d"

def test_string_with_consecutive_spaces_and_leading_trailing_spaces():
    assert fix_spaces("  a   b  ") == "--a-b-"

def test_long_string_with_multiple_consecutive_spaces_suite2():
    assert fix_spaces("This is a  very   long string with    multiple     consecutive spaces.") == "This_is_a-very--long_string_with---multiple-----consecutive_spaces."

def test_mixed_spaces_suite2():
    assert fix_spaces("Example  6  7") == "Example_6-7"