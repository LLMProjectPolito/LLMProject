
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

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces("Example 1 2") == "Example_1_2"

def test_consecutive_spaces_less_than_three():
    assert fix_spaces("Example  1") == "Example__1"

def test_consecutive_spaces_equal_to_three():
    assert fix_spaces("Example   1") == "Example-1"

def test_consecutive_spaces_more_than_three():
    assert fix_spaces("Example    1") == "Example-1"

def test_leading_spaces():
    assert fix_spaces(" Example") == "_Example"

def test_trailing_spaces():
    assert fix_spaces("Example ") == "Example_"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Example  ") == "_Example-"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example-1__2"

def test_empty_string():
    assert fix_spaces("") == ""

def test_string_with_only_spaces():
    assert fix_spaces("   ") == "---"

def test_string_with_special_characters():
    assert fix_spaces("Example!@#$%^&*() 1") == "Example!@#$%^&*()_1"