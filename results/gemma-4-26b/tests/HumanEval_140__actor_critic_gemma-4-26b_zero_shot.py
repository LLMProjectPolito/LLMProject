
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
import re

def fix_spaces(text):
    """
    Given a string text, replace all whitespace in it with underscores, 
    and if a string has more than 2 consecutive whitespace characters, 
    then replace all consecutive whitespace with - 
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    def replace_match(match):
        group = match.group(0)
        if len(group) > 2:
            return '-'
        else:
            return '_' * len(group)
    
    # Using \s+ to handle all whitespace (tabs, newlines, etc.) as per clarification
    return re.sub(r'\s+', replace_match, text)

@pytest.mark.parametrize("input_text, expected", [
    # Provided examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),

    # Edge Case: Empty string
    ("", ""),

    # Edge Case: No spaces (Redundancy removed)
    ("NoSpaces", "NoSpaces"),

    # Edge Case: Single space
    (" ", "_"),
    ("a b", "a_b"),

    # Edge Case: Exactly two spaces
    ("  ", "__"),
    ("a  b", "a__b"),

    # Edge Case: Exactly three spaces
    ("   ", "-"),
    ("a   b", "a-b"),

    # Edge Case: More than three spaces
    ("    ", "-"),
    ("a    b", "a-b"),

    # Edge Case: Leading and Trailing spaces
    (" leading", "_leading"),
    ("trailing ", "trailing_"),
    ("  leading", "__leading"),
    ("trailing  ", "trailing__"),
    ("   leading", "-leading"),
    ("trailing   ", "trailing-"),

    # Edge Case: Mixed patterns in one string
    ("a b  c   d", "a_b__c-d"),
    ("   a b  c", "-a_b__c"),
    ("a b  c   ", "a_b__c-"),

    # Edge Case: Whitespace characters (Tabs and Newlines)
    ("\t", "_"),
    ("a\tb", "a_b"),
    ("\t\t", "__"),
    ("\t\t\t", "-"),
    ("\n", "_"),
    ("a\n\nb", "a__b"),  # Fixed: \n\n is exactly 2 characters, should be underscores

    # Edge Case: Mixed Whitespace (Added)
    ("\t \n", "-"),

    # Edge Case: Unicode Whitespace (Added)
    ("\u00A0", "_"),
    ("\u00A0\u00A0\u00A0", "-"),

    # Edge Case: Non-alphanumeric characters
    ("! @ #", "!_@_#"),
    ("!   @  #", "!-@__#"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function against various scenarios including
    standard cases, boundary conditions, whitespace variations, and edge cases.
    """
    assert fix_spaces(input_text) == expected

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["a", "b"],
    {"text": "example"},
])
def test_fix_spaces_type_errors(invalid_input):
    """
    Tests that the function raises a TypeError when provided with non-string inputs.
    """
    with pytest.raises(TypeError):
        fix_spaces(invalid_input)