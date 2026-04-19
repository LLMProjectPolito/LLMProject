
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

@pytest.mark.parametrize("input_text, expected", [
    # Basic cases from docstring
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and No spaces
    ("", ""),
    ("NoSpacesHere", "NoSpacesHere"),
    
    # Single spaces in various positions
    (" ", "_"),
    ("Hello World", "Hello_World"),
    (" Hello", "_Hello"),
    ("Hello ", "Hello_"),
    
    # Exactly 2 spaces (Should be underscores because it's not MORE than 2)
    ("  ", "__"),
    ("Two  Spaces", "Two__Spaces"),
    
    # More than 2 spaces (3 or more should become a single hyphen)
    ("   ", "-"),
    ("Four    Spaces", "Four-Spaces"),
    ("Five     Spaces", "Five-Spaces"),
    
    # Mixed scenarios
    (" a  b   c    d", "_a__b-c-d"),
    ("   Leading and Trailing   ", "-Leading_and_Trailing-"),
    ("Multiple   sets of    spaces", "Multiple-sets_of-spaces"),
    ("One space, two  spaces, three   spaces", "One_space,_two__spaces,_three-spaces"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected