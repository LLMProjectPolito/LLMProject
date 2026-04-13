
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
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    # First, handle the cases with more than 2 consecutive spaces
    # We use a regex to find 3 or more spaces and replace them with a single hyphen
    text = re.sub(r' {3,}', '-', text)
    # Then, replace all remaining single or double spaces with underscores
    text = text.replace(' ', '_')
    return text

@pytest.mark.parametrize("input_text, expected", [
    # Basic examples
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and No Spaces
    ("", ""),
    ("NoSpacesHere", "NoSpacesHere"),
    ("12345", "12345"),
    
    # Boundary testing for consecutive spaces (1 or 2 -> _, 3+ -> -)
    (" ", "_"),               # 1 space
    ("  ", "__"),             # 2 spaces
    ("   ", "-"),             # 3 spaces
    ("    ", "-"),            # 4 spaces
    ("     ", "-"),           # 5 spaces
    
    # Positional testing (Start, Middle, End)
    ("   Start", "-Start"),            # Leading > 2
    ("End   ", "End-"),                # Trailing > 2
    ("  Both  ", "__Both__"),          # Leading/Trailing exactly 2
    ("   Both   ", "-Both-"),          # Leading/Trailing > 2
    
    # Mixed spacing scenarios
    ("a b  c   d    e", "a_b__c-d-e"), # 1, 2, 3, 4 spaces respectively
    ("  A   B  C    D", "__A-B__C-D"), # 2, 3, 2, 4 spaces
    ("Hello World  How   Are    You", "Hello_World__How-Are-You"),
    ("   Multiple   clusters   of spaces   ", "-Multiple-clusters-of_spaces-"),
    ("   1  2   3 4    5", "-1__2-3_4-5"),
    (" a b c ", "_a_b_c_"),
    ("  a  b  ", "__a__b__"),
])
def test_fix_spaces(input_text, expected):
    """
    Comprehensive test suite covering:
    1. Basic replacements (single space to underscore).
    2. Threshold testing (2 spaces vs 3 spaces).
    3. Positional testing (start, middle, end of string).
    4. String boundaries (empty strings, no spaces).
    5. Multiple mixed clusters of spaces.
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_non_space_whitespace():
    """
    Ensure that only literal spaces are replaced, 
    not tabs or newlines, as per the problem description.
    """
    text = "Tab\tSpace Space\nNewline"
    # \t remains \t, \n remains \n, " " becomes _
    expected = "Tab\tSpace_Space\nNewline"
    assert fix_spaces(text) == expected

def test_fix_spaces_idempotency():
    """
    Check if running the function again on its output changes the result.
    Since the output contains '_' and '-', and the function only looks for ' ',
    it should be idempotent.
    """
    input_text = "Example   with   many   spaces"
    first_pass = fix_spaces(input_text)
    second_pass = fix_spaces(first_pass)
    assert first_pass == second_pass

def test_fix_spaces_large_input():
    """Test with a larger string containing many variations of spaces."""
    input_text = "One " + " " * 1 + "Two " + " " * 2 + "Three " + " " * 3 + "Four " + " " * 10 + "Five"
    # One_Two__Three-Four-Five
    expected = "One_Two__Three-Four-Five"
    assert fix_spaces(input_text) == expected