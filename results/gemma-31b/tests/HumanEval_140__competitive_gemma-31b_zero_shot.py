
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
    
    # Edge cases: Empty and no spaces
    ("", ""),
    ("NoSpacesHere", "NoSpacesHere"),
    
    # Single and double spaces (should be underscores)
    ("single space", "single_space"),
    ("double  space", "double__space"),
    ("  leading", "__leading"),
    ("trailing  ", "trailing__"),
    
    # More than 2 consecutive spaces (should be hyphen)
    ("triple   space", "triple-space"),
    ("quadruple    space", "quadruple-space"),
    ("many       spaces", "many-spaces"),
    ("   leading_triple", "-leading_triple"),
    ("trailing_triple   ", "trailing_triple-"),
    
    # Mixed scenarios
    (" a  b   c    d ", "_a__b-c-d_"),
    ("one space, two  spaces, three   spaces", "one_space,_two__spaces,_three-spaces"),
    ("   ", "-"),
    ("  ", "__"),
    (" ", "_"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected