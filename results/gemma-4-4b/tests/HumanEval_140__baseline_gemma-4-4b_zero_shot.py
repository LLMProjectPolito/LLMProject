
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
    while "  " in text:
        text = text.replace("  ", "-")
    return text

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("This is a test", "This_is_a_test"),
        ("Multiple   spaces", "Multiple---spaces"),
        ("Leading and trailing spaces ", "_Leading_and_trailing_spaces_"),
        ("   Only spaces   ", "___Only_spaces___"),
        ("", ""),
        ("a b c", "a_b_c"),
        ("a   b   c", "a___b___c"),
        (" a  b   c ", "_a--b___c_"),
    ],
)
def test_fix_spaces_basic(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("   ", "___"),
        ("  ", "--"),
        (" ", "_"),
    ],
)
def test_fix_spaces_leading_trailing(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("a b c", "a_b_c"),
        ("a  b   c", "a--b___c"),
    ],
)
def test_fix_spaces_multiple(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output