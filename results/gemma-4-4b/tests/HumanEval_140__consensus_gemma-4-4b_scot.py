
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
    text = text.replace(" ", "_")
    while "   " in text:
        text = text.replace("   ", "-")
    return text

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("Multiple   spaces", "Multiple-spaces"),
        ("No spaces", "No spaces"),
        ("", ""),
        (" ", "_"),
        (" a b c ", "a_b_c_"),
        ("123 456", "123_456"),
        ("   ", "---"),
        ("  leading and trailing spaces  ", "__leading_and_trailing_spaces__"),
        ("  ", "---"),
        ("  a  b  c  ", "__a__b__c__"),
    ],
)
def test_fix_spaces(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output