import pytest
import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    Tabs and other whitespace characters are not modified.

    Examples:
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    return re.sub(r" {3,}", "-", text).replace(" ", "_")

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("Example", "Example"),
        ("Example 1", "Example_1"),
        (" Example 2", "_Example_2"),
        (" Example   3", "_Example-3"),
        ("", ""),
        ("NoSpaces", "NoSpaces"),
        ("  Leading and Trailing  ", "__Leading_and_Trailing__"),
        ("Multiple   Consecutive   Spaces", "Multiple-Consecutive-Spaces"),
        ("Mixed  Spaces  Here", "Mixed-Spaces_Here"),
        ("Mixed   Spaces   Here", "Mixed-Spaces-Here"),
        ("Mixed    Spaces    Here", "Mixed-Spaces-Here"),
        ("   ", "-"),
        ("    ", "-"),
        ("Two  Spaces", "Two_Spaces"),
        ("Tab\tand Space", "Tab\tand Space"),
        ("Exactly   Three", "Exactly-Three"),
        ("Four    Spaces", "Four-Spaces"),
        (" " * 100 + "SomeText" + " " * 50, "-" * 100 + "_SomeText_" + "-" * 50),
        ("Mixed  Spaces   Here", "Mixed-Spaces_Here"), # Test for order of operations
    ],
)
def test_fix_spaces(input_string, expected_output):
    assert fix_spaces(input_string) == expected_output

def test_fix_spaces_long_input():
    long_string = " " * 100 + "SomeText" + " " * 50
    assert fix_spaces(long_string) == "-" * 100 + "_SomeText_" + "-" * 50

def test_fix_spaces_tab_and_space():
    assert fix_spaces("Tab\tand Space") == "Tab\tand Space"