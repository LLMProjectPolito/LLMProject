
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
    ("Hello", "Hello"),
    ("HelloWorld", "HelloWorld"),
    
    # Consecutive space logic
    (" ", "_"),               # 1 space -> _
    ("  ", "__"),             # 2 spaces -> __ (not more than 2)
    ("   ", "-"),             # 3 spaces -> -
    ("    ", "-"),            # 4 spaces -> -
    ("     ", "-"),           # 5 spaces -> -
    
    # Mixed spacing
    ("a b", "a_b"),           # Single space
    ("a  b", "a__b"),         # Double space
    ("a   b", "a-b"),         # Triple space
    ("a    b", "a-b"),        # Quad space
    ("a b  c   d", "a_b__c-d"), # Mixed 1, 2, 3
    
    # Leading and trailing spaces
    ("  start", "__start"),
    ("   start", "-start"),
    ("end  ", "end__"),
    ("end   ", "end-"),
    ("  both  ", "__both__"),
    ("   both   ", "-both-"),
    
    # Complex strings
    ("The quick brown fox", "The_quick_brown_fox"),
    ("Too   many    spaces", "Too-many-spaces"),
    ("  Two  spaces  here  ", "__Two__spaces__here__"),
    ("   Three   spaces   here   ", "-Three-spaces-here-"),
    ("1 2  3   4    5", "1_2__3-4-5"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected