
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
    ("", ""),
    (" ", "_"),
    ("  ", "__"),
    ("   ", "-"),
    ("    ", "-"),
    ("a b", "a_b"),
    ("a  b", "a__b"),
    ("a   b", "a-b"),
    ("a    b", "a-b"),
    ("  a  ", "__a__"),
    ("   a   ", "-a-"),
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   leading", "-leading"),
    ("trailing   ", "trailing-"),
    ("multiple   spaces   here", "multiple-spaces-here"),
    ("mixed 1  2   3 4", "mixed_1__2-3_4"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected