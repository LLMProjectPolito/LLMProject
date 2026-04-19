
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
import re

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
    # Replace 3 or more consecutive spaces with a single hyphen
    text = re.sub(r' {3,}', '-', text)
    # Replace all remaining single or double spaces with underscores
    text = text.replace(' ', '_')
    return text

@pytest.mark.parametrize("input_text, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and no spaces
    ("", ""),
    ("NoSpaces", "NoSpaces"),
    
    # Single spaces
    (" ", "_"),
    ("Hello World", "Hello_World"),
    (" Hello", "_Hello"),
    ("World ", "World_"),
    
    # Exactly two spaces (should be underscores because not > 2)
    ("  ", "__"),
    ("Hello  World", "Hello__World"),
    
    # More than two spaces (3 or more -> replace block with '-')
    ("   ", "-"),
    ("Hello   World", "Hello-World"),
    ("Hello    World", "Hello-World"),
    ("Hello     World", "Hello-World"),
    
    # Mixed scenarios
    ("  Hello   World  ", "__Hello-World__"),
    (" a  b   c    d", "_a__b-c-d"),
    ("   Leading and trailing   ", "-Leading_and_trailing-"),
    ("One space, two  spaces, three   spaces", "One_space,_two__spaces,_three-spaces"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected