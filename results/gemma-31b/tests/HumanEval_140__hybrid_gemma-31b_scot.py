
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

# Note: fix_spaces is assumed to be defined in the environment.

@pytest.mark.parametrize("input_text, expected", [
    # --- Basic Cases ---
    ("Example", "Example"),                # No spaces
    ("Example 1", "Example_1"),            # Single space middle
    (" Example 2", "_Example_2"),          # Single space leading
    ("Example 2 ", "Example_2_"),          # Single space trailing
    ("A B C", "A_B_C"),                    # Multiple single spaces
    
    # --- Boundary Case: Exactly 2 spaces ---
    # Rule: 2 spaces -> __
    ("Two  Spaces", "Two__Spaces"),        # Two spaces middle
    ("  Two", "__Two"),                    # Two spaces leading
    ("Two  ", "Two__"),                    # Two spaces trailing
    ("  a  ", "__a__"),                    # Leading and trailing 2 spaces
    
    # --- Case: More than 2 spaces (3+) ---
    # Rule: 3+ spaces -> -
    ("Three   Spaces", "Three-Spaces"),    # Exactly 3
    ("Four    Spaces", "Four-Spaces"),     # Exactly 4
    ("Many      Spaces", "Many-Spaces"),   # Many spaces
    ("   Three", "-Three"),                # Leading 3+
    ("Three   ", "Three-"),                # Trailing 3+
    ("   a   ", "-a-"),                    # Leading and trailing 3+ spaces
    
    # --- Mixed Complexity ---
    (" Example   3", "_Example-3"),        # Mixed single and triple
    (" a  b   c    d", "_a__b-c-d"),       # Mixed 1, 2, 3, 4 spaces
    ("  a   b  c ", "__a-b__c_"),          # Leading/Trailing mixed (2, 3, 2, 1)
    (" a  b   c ", "_a__b-c_"),            # Complex mix
    ("1 2   3 4   5", "1_2-3_4-5"),        # Alternating patterns
    
    # --- Edge Cases: Only Spaces / Empty ---
    ("", ""),                              # Empty string
    (" ", "_"),                            # Only 1 space
    ("  ", "__"),                          # Only 2 spaces
    ("   ", "-"),                          # Only 3 spaces
    ("    ", "-"),                         # Only 4 spaces
])
def test_fix_spaces_parametrized(input_text, expected):
    """
    Comprehensive test of the fix_spaces logic covering the 1, 2, and 3+ 
    space replacement rules across various positions and combinations.
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_idempotency():
    """
    Verify that running the function on its own output does not change the result.
    Since underscores and hyphens are not spaces, they should not be processed.
    """
    original = "  Hello   World  "
    first_pass = fix_spaces(original)
    second_pass = fix_spaces(first_pass)
    assert first_pass == second_pass

def test_fix_spaces_non_space_whitespace():
    """
    Verify that the function only targets the space character ' ' 
    and ignores other whitespace like tabs or newlines.
    """
    text_with_tab = "Example\t1"
    text_with_newline = "Example\n1"
    assert fix_spaces(text_with_tab) == "Example\t1"
    assert fix_spaces(text_with_newline) == "Example\n1"

def test_fix_spaces_large_gap():
    """
    Ensure that an extremely large number of consecutive spaces 
    is collapsed into a single hyphen.
    """
    large_gap = "Word" + (" " * 100) + "Word"
    assert fix_spaces(large_gap) == "Word-Word"

def test_fix_spaces_no_mutation():
    """
    Ensure that strings containing no space characters remain entirely unchanged.
    """
    text = "NoSpacesHere123!@#$"
    assert fix_spaces(text) == text