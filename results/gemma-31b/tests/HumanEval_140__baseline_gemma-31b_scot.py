
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
    # Basic cases
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    ("Example 2 ", "Example_2_"),
    
    # Boundary case: Exactly 2 spaces (Should be underscores because 2 is not > 2)
    ("Example  2", "Example__2"),
    ("  Example", "__Example"),
    
    # More than 2 spaces (Should be hyphen)
    ("Example   3", "Example-3"),
    ("Example    4", "Example-4"),
    ("Example     5", "Example-5"),
    ("   Example", "-Example"),
    ("Example   ", "Example-"),
    
    # Edge cases: Empty and Space-only
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    
    # Mixed cases
    (" Example   3", "_Example-3"),
    (" a  b   c    d ", "_a__b-c-d_"),
    ("Hello   World  Test", "Hello-World__Test"),
    ("   Leading and Trailing   ", "-Leading_and_Trailing-"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function against various scenarios including 
    single, double, and triple+ spaces.
    """
    assert fix_spaces(input_text) == expected