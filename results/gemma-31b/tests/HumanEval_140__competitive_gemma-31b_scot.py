
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
    ("a b  c   d    e", "a_b__c-d-e"),
    ("   leading", "-leading"),
    ("trailing   ", "trailing-"),
    ("multiple   groups   of   spaces", "multiple-groups-of-spaces"),
    ("two  spaces", "two__spaces"),
    ("one space", "one_space"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected