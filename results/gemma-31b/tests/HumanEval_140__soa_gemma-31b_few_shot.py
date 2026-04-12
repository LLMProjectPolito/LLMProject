
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
    
    # Exactly two spaces (Not "more than 2", so should be underscores)
    ("  ", "__"),
    ("a  b", "a__b"),
    
    # More than two spaces (3 or more)
    ("   ", "-"),
    ("    ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("   a", "-a"),
    ("a   ", "a-"),
    
    # Mixed scenarios
    (" a  b   c    d ", "_a__b-c-d_"),
    ("  a   b  c ", "__a-b__c_"),
    ("one space,  two spaces,   three spaces", "one_space,___two_spaces,_-three_spaces"),
    ("   ", "-"),
    ("  ", "__"),
    (" ", "_"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected