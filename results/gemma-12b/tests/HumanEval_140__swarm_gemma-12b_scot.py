
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

def test_leading_and_trailing_spaces_with_consecutive():
    """
    Tests a string with leading and trailing spaces, and a sequence of more than 2 consecutive spaces in the middle.
    This tests the edge case where the function needs to handle both underscore replacement for leading/trailing spaces
    and hyphen replacement for consecutive spaces.
    """
    text = "  hello    world  "
    expected = "_hello-world_"
    assert fix_spaces(text) == expected

def test_leading_and_trailing_spaces_with_consecutive_2():
    """
    Tests a string with leading and trailing spaces, and also includes a sequence of more than 2 consecutive spaces in the middle.
    This tests the edge case where the function needs to handle both underscore replacement for leading/trailing spaces and dash replacement for consecutive spaces.
    """
    text = "  hello   world  "
    expected = "_hello-world_"
    assert fix_spaces(text) == expected

def test_leading_and_trailing_spaces_with_consecutive_3():
    """
    Tests a string with leading and trailing spaces, and also includes a sequence of more than 2 consecutive spaces in the middle.
    This tests the edge case where the function needs to handle both underscore replacement for single spaces and hyphen replacement for consecutive spaces,
    and also leading/trailing spaces.
    """
    text = "   Example   multiple   spaces   "
    expected = "-Example-multiple-spaces-"
    assert fix_spaces(text) == expected