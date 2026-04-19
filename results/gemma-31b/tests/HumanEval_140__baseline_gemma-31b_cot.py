
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
    # Provided examples
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
    
    # Two consecutive spaces (should be underscores as it's not > 2)
    ("  ", "__"),
    ("a  b", "a__b"),
    ("  a", "__a"),
    ("a  ", "a__"),
    
    # Three or more consecutive spaces (should be replaced by a single '-')
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("   a", "-a"),
    ("a   ", "a-"),
    
    # Mixed space sequences
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  a   b  c ", "__a-b__c_"),
    ("   a   b   ", "-a-b-"),
    
    # Strings with other characters
    ("Hello World!", "Hello_World!"),
    ("123   456  789 0", "123-456__789_0"),
    ("Special @#$   Chars", "Special_@#$-Chars"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function based on the following rules:
    1. Single spaces are replaced by underscores.
    2. Two consecutive spaces are replaced by two underscores.
    3. Three or more consecutive spaces are replaced by a single hyphen.
    """
    assert fix_spaces(input_text) == expected