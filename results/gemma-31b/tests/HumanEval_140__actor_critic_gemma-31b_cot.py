
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
    
    # Edge Case: Empty string
    ("", ""),
    
    # Edge Case: Single space
    (" ", "_"),
    
    # Edge Case: Exactly two spaces (Not "more than 2", so should be underscores)
    ("  ", "__"),
    ("a  b", "a__b"),
    
    # Edge Case: More than two spaces (3, 4, 5...)
    ("   ", "-"),
    ("    ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    
    # Edge Case: Leading and trailing spaces
    (" a", "_a"),
    ("a ", "a_"),
    ("  a", "__a"),
    ("a  ", "a__"),
    ("   a", "-a"),
    ("a   ", "a-"),
    
    # Complex mixed cases
    (" a  b   c    d e", "_a__b-c-d_e"),
    ("Hello World  Test   Case    Final", "Hello_World__Test-Case-Final"),
    ("   Leading and trailing   ", "-Leading_and_trailing-"),
    
    # Non-space characters and special characters
    ("!@# $ %  ^ &   *()", "!@#_$_%__^_&_-*()"),
    ("123 456  789   0", "123_456__789-0"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function against various scenarios including:
    - No spaces
    - Single spaces (replaced by _)
    - Double spaces (replaced by __)
    - Triple or more spaces (replaced by -)
    - Leading/Trailing spaces
    - Empty strings
    """
    assert fix_spaces(input_text) == expected