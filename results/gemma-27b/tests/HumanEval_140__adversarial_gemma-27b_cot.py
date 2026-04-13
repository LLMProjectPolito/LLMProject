
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

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_space():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_trailing_space():
    assert fix_spaces("Example 4 ") == "Example_4_"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example 5 ") == "_Example_5_"

def test_multiple_leading_spaces():
    assert fix_spaces("   Example 6") == "---Example_6"

def test_multiple_trailing_spaces():
    assert fix_spaces("Example 7   ") == "Example_7---"

def test_multiple_consecutive_spaces():
    assert fix_spaces("Example   4   5") == "Example-4-5"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "---"

def test_mixed_spaces():
    assert fix_spaces("  Example    7  ") == "--Example-7--"

def test_string_with_tabs():
    assert fix_spaces("Example\t8") == "Example_8"

def test_string_with_newlines():
    assert fix_spaces("Example\n9") == "Example_9"

def test_long_string_with_multiple_spaces():
    long_string = "This is a very long string with   many   spaces   in it."
    expected_string = "This_is_a_very_long_string-with-many-spaces-in_it."
    assert fix_spaces(long_string) == expected_string