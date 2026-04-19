
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
    
    # Edge Case: Single space (should be underscore)
    (" ", "_"),
    
    # Edge Case: Two consecutive spaces (not > 2, so should be underscores)
    ("  ", "__"),
    
    # Edge Case: Three consecutive spaces (is > 2, should be dash)
    ("   ", "-"),
    
    # Edge Case: More than three consecutive spaces (should be dash)
    ("    ", "-"),
    ("     ", "-"),
    
    # Mixed cases: combinations of 1, 2, and 3+ spaces
    ("a b", "a_b"),             # 1 space
    ("a  b", "a__b"),           # 2 spaces
    ("a   b", "a-b"),           # 3 spaces
    ("a    b", "a-b"),          # 4 spaces
    ("a b  c   d    e", "a_b__c-d-e"), # 1, 2, 3, 4 spaces
    
    # Leading and trailing spaces
    (" a", "_a"),
    ("a ", "a_"),
    ("  a", "__a"),
    ("   a", "-a"),
    ("a  ", "a__"),
    ("a   ", "a-"),
    
    # Complex mixed string
    ("  Hello   World  Pytest   ", "__Hello-World__Pytest-"),
    
    # Strings with no spaces
    ("Python", "Python"),
    ("12345", "12345"),
    ("!@#$%^&*()", "!@#$%^&*()"),
    
    # Strings with other whitespace (should remain unchanged as the prompt specifies "spaces")
    ("Hello\tWorld", "Hello\tWorld"),
    ("Hello\nWorld", "Hello\nWorld"),
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