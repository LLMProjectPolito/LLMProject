
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

def test_fix_spaces_empty():
    assert fix_spaces("") == ""

def test_fix_spaces_single_space():
    assert fix_spaces(" ") == " "

def test_fix_spaces_multiple_spaces():
    assert fix_spaces("  ") == "  "

def test_fix_spaces_consecutive_spaces():
    assert fix_spaces("  ") == "-"

def test_fix_spaces_mixed_spaces():
    assert fix_spaces("  hello world") == "hello   world"

def test_fix_spaces_no_spaces():
    assert fix_spaces("no spaces") == "no spaces"

def test_fix_spaces_with_underscores():
    assert fix_spaces("hello_world") == "hello_world"

def test_fix_spaces_with_hyphens():
    assert fix_spaces("hello-world") == "hello-world"