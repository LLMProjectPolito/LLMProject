
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
    # Basic cases from the problem description
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and No Spaces
    ("", ""),
    ("Hello", "Hello"),
    ("Hello World", "Hello_World"),
    
    # Edge cases: Space counts
    (" ", "_"),           # 1 space -> _
    ("  ", "__"),         # 2 spaces -> __
    ("   ", "-"),         # 3 spaces -> -
    ("    ", "-"),        # 4 spaces -> -
    ("     ", "-"),       # 5 spaces -> -
    
    # Mixed space sequences
    ("a b", "a_b"),               # Single space
    ("a  b", "a__b"),             # Double space
    ("a   b", "a-b"),             # Triple space
    ("a    b", "a-b"),            # Quadruple space
    ("a b  c   d    e", "a_b__c-d-e"), # Mixed 1, 2, 3, 4
    
    # Leading and Trailing spaces
    ("  a", "__a"),               # Leading double
    ("   a", "-a"),               # Leading triple
    ("a  ", "a__"),               # Trailing double
    ("a   ", "a-"),               # Trailing triple
    ("  a  ", "__a__"),           # Leading and trailing double
    ("   a   ", "-a-"),           # Leading and trailing triple
    
    # Complex combinations
    ("  a   b  c    d ", "__a-b__c-d_"),
    ("   ", "-"),                 # Only spaces (3)
    ("  ", "__"),                 # Only spaces (2)
    (" ", "_"),                   # Only spaces (1)
    
    # Non-space characters and whitespace
    ("a\tb", "a\tb"),             # Tabs should not be treated as spaces
    ("a\na", "a\na"),             # Newlines should not be treated as spaces
    (" a b ", "_a_b_"),           # Simple wrap
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function against various edge cases.
    Logic:
    - 1 space -> '_'
    - 2 spaces -> '__'
    - 3 or more spaces -> '-'
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_large_input():
    """Test with a larger string to ensure performance and consistency."""
    input_text = "word " * 100 + "   " + "word " * 100
    # 100 groups of "word " (1 space) + 1 group of 3 spaces + 100 groups of "word "
    # Result: 100 * "word_" + "-" + 100 * "word_"
    expected = "word_" * 100 + "-" + "word_" * 100
    assert fix_spaces(input_text) == expected

def test_fix_spaces_no_mutation():
    """Ensure the function handles strings without spaces correctly."""
    text = "NoSpacesHere123!"
    assert fix_spaces(text) == text