
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
    ("  a  b   c    d ", "__a__b-c-d_"),
    ("  a   b  c    d ", "__a-b__c-d_"),
    ("  a   b  ", "__a-b__"),
])
def test_fix_spaces_boundary_conditions(input_str, expected):
    assert fix_spaces(input_str) == expected