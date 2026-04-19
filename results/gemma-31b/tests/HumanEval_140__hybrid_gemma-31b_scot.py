
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

# The function fix_spaces is assumed to be defined elsewhere.

@pytest.mark.parametrize("input_text, expected_output", [
    # --- Basic & No Space Scenarios ---
    ("Example", "Example"),                # No spaces
    ("Example 1", "Example_1"),            # Single space -> underscore
    ("Example  1", "Example__1"),          # Double space -> two underscores
    
    # --- Rule B: 3 or more consecutive spaces -> single hyphen ---
    ("Example   1", "Example-1"),          # Exactly 3 spaces
    ("Example    1", "Example-1"),         # 4 spaces
    ("Example     1", "Example-1"),        # 5 spaces
    ("Example          1", "Example-1"),   # Many spaces
    
    # --- Positional Scenarios (Leading/Trailing) ---
    (" Example", "_Example"),              # Leading single
    ("  Example", "__Example"),            # Leading double
    ("   Example", "-Example"),            # Leading triple
    ("Example ", "Example_"),              # Trailing single
    ("Example  ", "Example__"),            # Trailing double
    ("Example   ", "Example-"),            # Trailing triple
    
    # --- Mixed Patterns ---
    (" Example   3", "_Example-3"),        # Mixed 1 and 3
    (" a  b   c    d", "_a__b-c-d"),       # 1, 2, 3, 4 spaces respectively
    ("  hello   world  ", "__hello-world__"), # 2 leading, 3 middle, 2 trailing
    ("one  two   three four", "one__two-three_four"), # 2, 3, 1 spaces
    (" A  B   C    D ", "_A__B-C-D_"),     # Mixed: 1, 2, 3, 4, 1
    
    # --- Edge Cases ---
    ("", ""),                              # Empty string
    (" ", "_"),                            # Single space only
    ("  ", "__"),                          # Double space only
    ("   ", "-"),                          # Triple space only
    ("    ", "-"),                         # Multiple spaces only
])
def test_fix_spaces_parametrized(input_text, expected_output):
    """
    Comprehensive test for the core logic of fix_spaces, covering 
    single, double, and triple+ space replacement rules.
    """
    assert fix_spaces(input_text) == expected_output

def test_fix_spaces_whitespace_handling():
    """
    Ensure that only literal space characters ' ' are replaced.
    Tabs, newlines, and other whitespace should remain untouched.
    """
    # Test purely non-space whitespace
    assert fix_spaces("Example\t1\n2") == "Example\t1\n2"
    # Test spaces mixed with other whitespace
    assert fix_spaces(" \n\t ") == "_\n\t_"

def test_fix_spaces_large_input():
    """
    Stress test with a larger string containing alternating patterns 
    to ensure performance and correctness at scale.
    """
    input_text = "word " * 100 + "   " + "word " * 100
    # 100 single spaces (each becomes _), one block of 3 (becomes -), 100 single spaces
    expected = ("word_" * 100) + "-" + ("word_" * 100)
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_stability():
    """
    Verify that the function consistently returns a string for valid string inputs.
    """
    assert isinstance(fix_spaces("test"), str)
    assert isinstance(fix_spaces("   "), str)
    assert isinstance(fix_spaces(""), str)

def test_fix_spaces_idempotency():
    """
    Verify that characters already representing the 'fixed' state 
    (underscores and dashes) are not altered by the function.
    """
    text = "Already_Fixed-Example"
    assert fix_spaces(text) == text