import pytest

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
    if "   " in text:
        text = text.replace("   ", "-")
        while "  " in text:
            text = text.replace("  ", "-")
        text = text.replace(" ", "_")
    else:
        text = text.replace(" ", "_")
    return text

# STEP 1: REASONING
# The function `fix_spaces` aims to replace spaces in a string with underscores,
# but handles consecutive spaces differently.  More than two consecutive spaces
# should be replaced with a single hyphen.  The tests should cover:
# - No spaces
# - Single spaces
# - Leading/trailing spaces
# - Two consecutive spaces
# - Three or more consecutive spaces
# - Combinations of these cases

# STEP 2: PLAN
# Test function names and scenarios:
# - test_no_spaces: String with no spaces.
# - test_single_spaces: String with single spaces between words.
# - test_leading_trailing_spaces: String with leading and trailing spaces.
# - test_two_consecutive_spaces: String with exactly two consecutive spaces.
# - test_three_consecutive_spaces: String with three consecutive spaces.
# - test_more_than_three_consecutive_spaces: String with more than three consecutive spaces.
# - test_mixed_spaces: String with a mix of single, double, and multiple spaces.
# - test_empty_string: Empty string.
# - test_only_spaces: String containing only spaces.
# - test_leading_and_multiple_spaces: Leading spaces and multiple spaces in the middle.

# STEP 3: CODE
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_trailing_spaces():
    assert fix_spaces(" Example 2 ") == "_Example_2_"

def test_two_consecutive_spaces():
    assert fix_spaces("Example  1") == "Example__1"

def test_three_consecutive_spaces():
    assert fix_spaces("Example   1") == "Example-1"

def test_more_than_three_consecutive_spaces():
    assert fix_spaces("Example    1") == "Example-1"

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_empty_string():
    assert fix_spaces("") == ""

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_leading_and_multiple_spaces():
    assert fix_spaces("   Example   1") == "-Example-1"

def test_multiple_spaces_at_end():
    assert fix_spaces("Example   ") == "Example-"

def test_multiple_spaces_at_beginning():
    assert fix_spaces("   Example") == "-Example"

def test_consecutive_spaces_and_leading():
    assert fix_spaces("  Example   1") == "__Example-1"