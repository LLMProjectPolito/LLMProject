
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
    
    # Edge cases: Empty and whitespace only
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    
    # Mixed space counts
    ("a b", "a_b"),           # 1 space
    ("a  b", "a__b"),         # 2 spaces (not more than 2)
    ("a   b", "a-b"),         # 3 spaces (more than 2)
    ("a    b", "a-b"),        # 4 spaces (more than 2)
    ("a b  c   d    e", "a_b__c-d-e"),
    
    # Position tests
    (" leading", "_leading"),
    ("   leading", "-leading"),
    ("trailing ", "trailing_"),
    ("trailing   ", "trailing-"),
    ("  both  ", "__both__"),
    ("   both   ", "-both-"),
    
    # Complex strings
    ("Hello World  This is   a test", "Hello_World__This_is-a_test"),
    ("   Multiple   spaces   here   ", "-Multiple-spaces-here-"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected