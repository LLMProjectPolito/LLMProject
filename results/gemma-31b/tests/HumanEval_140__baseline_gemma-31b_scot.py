
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
    
    # Edge Case: No spaces
    ("Pytest", "Pytest"),
    ("", ""),
    
    # Edge Case: Exactly 1 space
    ("a b", "a_b"),
    
    # Edge Case: Exactly 2 spaces (Not "more than 2", so should be underscores)
    ("a  b", "a__b"),
    
    # Edge Case: More than 2 spaces (3, 4, 5...)
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    
    # Edge Case: Leading and Trailing spaces
    (" hello", "_hello"),
    ("hello ", "hello_"),
    ("   hello", "-hello"),
    ("hello   ", "hello-"),
    ("  hello", "__hello"),
    ("hello  ", "hello__"),
    
    # Edge Case: Mixed space lengths
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   a  b   ", "-a__b-"),
    
    # Edge Case: Only spaces
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function against various space configurations
    to ensure correct replacement of spaces with underscores or hyphens.
    """
    assert fix_spaces(input_text) == expected