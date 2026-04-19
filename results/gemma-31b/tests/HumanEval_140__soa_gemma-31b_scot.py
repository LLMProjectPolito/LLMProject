
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
    
    # Single space cases
    (" ", "_"),
    ("a b", "a_b"),
    (" a", "_a"),
    ("a ", "a_"),
    
    # Two consecutive spaces (should be underscores because it's not MORE than 2)
    ("  ", "__"),
    ("a  b", "a__b"),
    ("  a", "__a"),
    ("a  ", "a__"),
    
    # Three or more consecutive spaces (should be hyphen)
    ("   ", "-"),
    ("    ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("   a", "-a"),
    ("a   ", "a-"),
    
    # Mixed scenarios
    (" a  b   c    d ", "_a__b-c-d_"),
    ("Hello World  Test   Case", "Hello_World__Test-Case"),
    ("   Multiple   Spaces   Here   ", "-Multiple-Spaces-Here-"),
    ("1 2  3   4    5", "1_2__3-4-5"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected