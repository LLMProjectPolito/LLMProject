
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

def test_trailing_space():
    assert fix_spaces("Example 2 ") == "Example_2_"

def test_multiple_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_multiple_spaces_at_beginning():
    assert fix_spaces("   Example 3") == "-Example_3"

def test_multiple_spaces_at_end():
    assert fix_spaces("Example 3   ") == "Example_3-"

def test_multiple_spaces_mixed():
    assert fix_spaces("  Example   4  ") == "-Example-4-"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_two_consecutive_spaces():
    assert fix_spaces("Example  4") == "Example__4"

def test_long_string_with_multiple_space_groups():
    assert fix_spaces("This is a long string with   multiple    space groups.") == "This_is_a_long_string_with-multiple-space_groups."

def test_string_with_tabs():
    assert fix_spaces("Example\t1") == "Example_1"

def test_string_with_newlines():
    assert fix_spaces("Example\n1") == "Example_1"

def test_string_with_mixed_whitespace():
    assert fix_spaces("Example \t\n 1") == "Example_-1"

def test_string_with_only_consecutive_spaces():
    assert fix_spaces("     ") == "-"

def test_string_with_three_consecutive_spaces():
    assert fix_spaces("Example 1 2  3") == "Example_1_2__3"

def test_string_with_four_consecutive_spaces():
    assert fix_spaces("Example 1 2   3") == "Example_1_2-3"