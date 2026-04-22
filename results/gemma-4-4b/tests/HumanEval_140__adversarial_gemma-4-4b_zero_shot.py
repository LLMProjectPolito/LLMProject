
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
    "input_text, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("  Hello  World  ", "__Hello---World__"),
        ("This is a test", "This_is_a_test"),
        ("Multiple   spaces", "Multiple---spaces"),
        ("Leading and trailing spaces ", "_Leading-and-trailing-spaces_"),
        ("   ", "___"),
        ("", ""),
        ("One", "One"),
        ("  One  ", "__One__"),
        ("  One   Two  ", "__One---Two__"),
        ("  One   Two   Three  ", "__One---Two---Three__"),
        ("A B C", "A_B_C"),
        ("A   B   C", "A___B___C"),
    ],
)
def test_fix_spaces(input_text, expected_output):
    assert fix_spaces(input_text) == expected_output

def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("NoSpaces") == "NoSpaces"

def test_leading_and_trailing_spaces():
    assert fix_spaces(" Leading and trailing ") == "_Leading-and-trailing_ "

def test_multiple_consecutive_spaces():
    assert fix_spaces("  Multiple   consecutive   spaces  ") == "__Multiple---consecutive---spaces__"

def test_mixed_spaces_and_other_characters():
    assert fix_spaces("  a b c   d e f  ") == "_a_b_c---d_e_f_"