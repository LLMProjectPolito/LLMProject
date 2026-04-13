
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
    
    # Single space variations
    (" ", "_"),
    ("Hello World", "Hello_World"),
    (" Leading", "_Leading"),
    ("Trailing ", "Trailing_"),
    
    # Exactly two spaces (Should be underscores because it's not MORE than 2)
    ("  ", "__"),
    ("Two  Spaces", "Two__Spaces"),
    ("  Start", "__Start"),
    ("End  ", "End__"),
    
    # More than two spaces (3 or more should become a single hyphen)
    ("   ", "-"),
    ("Three   Spaces", "Three-Spaces"),
    ("Four    Spaces", "Four-Spaces"),
    ("Many      Spaces", "Many-Spaces"),
    ("   Start", "-Start"),
    ("End   ", "End-"),
    
    # Mixed scenarios
    (" A  B   C    D ", "_A__B-C-D_"),
    ("Multiple   spaces and  single spaces", "Multiple-spaces_and__single_spaces"),
    ("   Leading and Trailing   ", "-Leading_and_Trailing-"),
    ("1 2  3   4    5", "1_2__3-4-5"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected