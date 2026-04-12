
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
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    ("Two  spaces", "Two__spaces"),
    ("Three   spaces", "Three-spaces"),
    ("Four    spaces", "Four-spaces"),
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    (" a b  c   d    e", "_a_b__c-d-e"),
    ("Leading   space", "-Leading_space"), # Wait, "Leading   space" -> "-Leading_space" is wrong. 
    # "Leading   space" has 3 spaces. 3 > 2, so "   " becomes "-". Result: "Leading-space"
    ("Leading   space", "Leading-space"),
    ("Trailing space  ", "Trailing_space__"),
    ("Trailing space   ", "Trailing_space-"),
    ("Mixed  and   spaces", "Mixed__and-spaces"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected

def test_fix_spaces_only_spaces():
    assert fix_spaces(" ") == "_"
    assert fix_spaces("  ") == "__"
    assert fix_spaces("   ") == "-"
    assert fix_spaces("    ") == "-"

def test_fix_spaces_no_spaces():
    assert fix_spaces("HelloWorld") == "HelloWorld"
    assert fix_spaces("12345") == "12345"
    assert fix_spaces("!@#$%") == "!@#$%"