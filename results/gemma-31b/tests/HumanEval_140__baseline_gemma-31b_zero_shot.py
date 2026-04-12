
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
    # Basic cases from docstring
    ("Example", "Example"),
    ("Example 1", "Example_1"),
    (" Example 2", "_Example_2"),
    (" Example   3", "_Example-3"),
    
    # Edge cases: Empty and No spaces
    ("", ""),
    ("NoSpacesHere", "NoSpacesHere"),
    
    # Testing the "more than 2" threshold (2 spaces vs 3 spaces)
    ("Two spaces", "Two_spaces"),
    ("Two  spaces", "Two__spaces"), # Exactly 2: should be underscores
    ("Three   spaces", "Three-spaces"), # 3: more than 2, should be hyphen
    ("Four    spaces", "Four-spaces"), # 4: more than 2, should be hyphen
    ("Many       spaces", "Many-spaces"), # Many: more than 2, should be hyphen
    
    # Leading and Trailing spaces
    (" leading", "_leading"),
    ("  leading", "__leading"),
    ("   leading", "-leading"),
    ("trailing ", "trailing_"),
    ("trailing  ", "trailing__"),
    ("trailing   ", "trailing-"),
    
    # Mixed combinations
    (" a  b   c    d ", "_a__b-c-d_"),
    ("   start and end   ", "-start_and_end-"),
    ("multiple   groups   of spaces", "multiple-groups-of_spaces"),
])
def test_fix_spaces(input_text, expected):
    assert fix_spaces(input_text) == expected