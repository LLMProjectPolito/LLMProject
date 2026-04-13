
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
    
    # Edge cases: Empty and whitespace only
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("     ", "-"),
    
    # Consecutive spaces logic
    ("a b", "a_b"),
    ("a  b", "a__b"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    
    # Mixed spacing
    (" a  b   c    d ", "_a__b-c-d_"),
    ("Hello World  Test   Case", "Hello_World__Test-Case"),
    ("   Leading", "-Leading"),
    ("Trailing   ", "Trailing-"),
    
    # Non-space whitespace (should remain unchanged based on "spaces" requirement)
    ("Example\t1", "Example\t1"),
    ("Example\n1", "Example\n1"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected