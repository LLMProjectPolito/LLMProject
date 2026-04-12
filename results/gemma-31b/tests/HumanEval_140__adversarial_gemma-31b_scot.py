
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

# The function fix_spaces is provided by the environment; we are testing it.

@pytest.mark.parametrize("input_text, expected", [
    # Basic cases from docstring
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # No spaces
    ("", ""),
    ("Python", "Python"),
    ("12345", "12345"),
    
    # Single spaces (should be underscores)
    (" ", "_"),
    ("a b", "a_b"),
    (" a ", "_a_"),
    ("a b c", "a_b_c"),
    
    # Double spaces (Boundary: NOT more than 2, so should be underscores)
    ("  ", "__"),
    ("a  b", "a__b"),
    ("  a", "__a"),
    ("a  ", "a__"),
    
    # Triple spaces (Boundary: more than 2, should be hyphen)
    ("   ", "-"),
    ("a   b", "a-b"),
    ("   a", "-a"),
    ("a   ", "a-"),
    
    # More than triple spaces (should still be a single hyphen)
    ("    ", "-"),
    ("a    b", "a-b"),
    ("a     b", "a-b"),
    ("a          b", "a-b"),
    
    # Mixed scenarios
    ("a b  c   d    e", "a_b__c-d-e"),
    ("  a   b  c ", "__a-b__c_"),
    ("   a  b ", "-a__b_"),
    ("a b  c   d", "a_b__c-d"),
])
def test_fix_spaces_logic(input_text, expected):
    """
    Tests the fix_spaces function against various space configurations
    to ensure correct replacement of single, double, and 3+ spaces.
    """
    assert fix_spaces(input_text) == expected

def test_fix_spaces_type_stability():
    """
    Ensure the function returns a string even for empty inputs.
    """
    result = fix_spaces("")
    assert isinstance(result, str)

def test_fix_spaces_non_space_whitespace():
    """
    The requirement specifically mentions 'spaces'. 
    Tabs or newlines should generally be left alone unless specified.
    """
    # If the function is strictly for ' ', \t should remain \t
    text = "Example\t1"
    # We assume only ' ' is targeted based on the prompt
    assert fix_spaces(text) == "Example\t1"