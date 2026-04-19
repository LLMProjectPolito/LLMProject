
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
    (" a ", "_a_"),
    
    # Exactly two spaces (should be underscores because it's not MORE than 2)
    ("  ", "__"),
    ("a  b", "a__b"),
    ("  a", "__a"),
    ("a  ", "a__"),
    
    # More than two spaces (should be hyphen)
    ("   ", "-"),
    ("    ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("   a", "-a"),
    ("a   ", "a-"),
    
    # Mixed sequences
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  a   b  c    d ", "__a-b__c-d_"),
    ("   ", "-"),
    ("  ", "__"),
    (" ", "_"),
    
    # Complex combinations
    ("Hello World  Test   Case    Final", "Hello_World__Test-Case-Final"),
    ("   Leading and trailing   ", "-Leading_and_trailing-"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected