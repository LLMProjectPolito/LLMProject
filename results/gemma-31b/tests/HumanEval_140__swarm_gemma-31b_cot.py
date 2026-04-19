
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
import math

@pytest.mark.parametrize("input_str, expected", [
    ("  a   b  ", "__a-b__"),
    ("  a  b   c    d ", "__a__b-c-d_"),
])
def test_fix_spaces_consecutive_counts(input_str, expected):
    """
    Tests the boundary between 2 consecutive spaces (should become underscores) 
    and 3 or more consecutive spaces (should become a single dash).
    """
    assert fix_spaces(input_str) == expected