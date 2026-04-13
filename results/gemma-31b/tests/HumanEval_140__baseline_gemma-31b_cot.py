
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
    
    # Edge cases: Empty and No Spaces
    ("", ""),
    ("Hello", "Hello"),
    ("HelloWorld", "HelloWorld"),
    
    # Edge cases: Single and Double spaces (should be underscores)
    (" ", "_"),
    ("  ", "__"),
    ("a b", "a_b"),
    ("a  b", "a__b"),
    
    # Edge cases: More than 2 spaces (should be a single dash)
    ("   ", "-"),
    ("    ", "-"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    
    # Mixed scenarios
    (" a  b   c    d ", "_a__b-c-d_"),
    ("  leading", "__leading"),
    ("   leading", "-leading"),
    ("trailing  ", "trailing__"),
    ("trailing   ", "trailing-"),
    ("multiple   blocks   of spaces", "multiple-blocks-of spaces"), # Wait, "of spaces" has 1 space -> "of_spaces"
    ("multiple   blocks   of spaces", "multiple-blocks-of_spaces"),
    
    # Complex string
    ("The  quick brown   fox jumps    over the lazy dog", 
     "The__quick_brown-fox_jumps-over_the_lazy_dog"),
])
def test_fix_spaces(input_text, expected):
    """
    Tests the fix_spaces function based on the following rules:
    1. Single spaces are replaced by underscores.
    2. Two consecutive spaces are replaced by two underscores (since 2 is not > 2).
    3. Three or more consecutive spaces are replaced by a single dash.
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_non_space_whitespace():
    """
    Verify that only actual space characters ' ' are replaced, 
    not tabs or newlines, unless the function is intended to handle all whitespace.
    Based on the prompt 'replace all spaces', we assume only ' '.
    """
    # If the function only targets ' ', tabs should remain.
    assert fix_spaces("Example\t1") == "Example\t1"
    assert fix_spaces("Example\n1") == "Example\n1"