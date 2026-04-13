
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

def test_fix_spaces_with_leading_and_trailing_spaces_and_multiple_consecutive_spaces():
    """Test case for leading/trailing spaces and multiple consecutive spaces."""
    assert fix_spaces("   abc  def   ") == "-abc-def-"