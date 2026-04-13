
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

# The function fix_spaces is assumed to be defined in the environment.

@pytest.mark.parametrize("input_text, expected", [
    # Docstring examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # No spaces / Empty string
    ("", ""),
    ("Hello", "Hello"),
    ("12345", "12345"),
    
    # Boundary cases: 1, 2, and 3 spaces
    ("a b", "a_b"),          # 1 space -> _
    ("a  b", "a__b"),        # 2 spaces -> __
    ("a   b", "a-b"),        # 3 spaces -> -
    
    # More than 3 spaces
    ("a    b", "a-b"),       # 4 spaces -> -
    ("a     b", "a-b"),      # 5 spaces -> -
    ("a          b", "a-b"), # 10 spaces -> -
    ("a" + " " * 100 + "b", "a-b"), # Complexity: 100 spaces -> -
    
    # Positional spaces (Start/End)
    (" test", "_test"),      # Leading single
    ("  test", "__test"),    # Leading double
    ("   test", "-test"),    # Leading triple
    ("test ", "test_"),      # Trailing single
    ("test  ", "test__"),    # Trailing double
    ("test   ", "test-"),    # Trailing triple
    
    # Mixed sequences
    ("a b  c   d    e", "a_b__c-d-e"), 
    ("   a   b   ", "-a-b-"),
    ("  a b  ", "__a_b__"),
    
    # Whitespace only
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function against various scenarios including 
    docstring examples, boundary conditions, and long sequences.
    """
    assert fix_spaces(input_text) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    45.67,
    ["a", "b"],
    {"text": "hello"},
])
def test_fix_spaces_invalid_types(invalid_input):
    """
    Verify that the function raises a TypeError when provided with non-string inputs.
    """
    with pytest.raises(TypeError):
        fix_spaces(invalid_input)

@pytest.mark.parametrize("whitespace_text, expected", [
    ("a\tb", "a\tb"),       # Tab should not be replaced
    ("a\nb", "a\nb"),       # Newline should not be replaced
    ("a\rb", "a\rb"),       # Carriage return should not be replaced
    (" a\t b ", "_a\t_b_"), # Mixed space and tab
])
def test_fix_spaces_other_whitespace(whitespace_text, expected):
    """
    Ensure that only literal space characters (' ') are replaced, 
    and other whitespace characters remain untouched.
    """
    assert fix_spaces(whitespace_text) == expected