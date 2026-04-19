
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

@pytest.mark.parametrize("input_text, expected_output", [
    ("two  spaces three   spaces", "two__spaces_three-spaces"),
    (" a  b   c    d ", "_a__b-c-d_"),
    ("  a   b  c    d ", "__a-b__c-d_"),
])
def test_fix_spaces_consecutive_thresholds(input_text, expected_output):
    """
    Tests the boundary logic for space replacement:
    1 space -> _
    2 spaces -> __
    3 or more spaces -> -
    """
    assert fix_spaces(input_text) == expected_output