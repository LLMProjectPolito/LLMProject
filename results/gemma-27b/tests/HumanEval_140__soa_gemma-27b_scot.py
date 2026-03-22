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
# should be replaced with a single hyphen.  The tests need to cover:
# - Strings with no spaces
# - Strings with single spaces
# - Strings with leading/trailing spaces
# - Strings with exactly two consecutive spaces
# - Strings with more than two consecutive spaces
# - Edge cases like empty strings.

# STEP 2: PLAN
# Test function names and scenarios:
# - test_no_spaces: String with no spaces.
# - test_single_spaces: String with single spaces between words.
# - test_leading_trailing_spaces: String with leading and trailing spaces.
# - test_two_consecutive_spaces: String with exactly two consecutive spaces.
# - test_more_than_two_consecutive_spaces: String with more than two consecutive spaces.
# - test_empty_string: Empty string.
# - test_mixed_spaces: String with a mix of single, double, and more than two consecutive spaces.
# - test_multiple_occurrences: String with multiple occurrences of consecutive spaces.

# STEP 3: CODE
def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_spaces():
    assert fix_spaces("Example 1") == "Example_1"

def test_leading_trailing_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_two_consecutive_spaces():
    assert fix_spaces("Example  1") == "Example__1"

def test_more_than_two_consecutive_spaces():
    assert fix_spaces("Example   3") == "_Example-3"

def test_empty_string():
    assert fix_spaces("") == ""

def test_mixed_spaces():
    assert fix_spaces("Example  1   2") == "Example__1-2"

def test_multiple_occurrences():
    assert fix_spaces("  Example   1  2   3  ") == "_Example-1_2-3_"

def test_only_spaces():
    assert fix_spaces("   ") == "-"

def test_long_consecutive_spaces():
    assert fix_spaces("Example     1") == "_Example-1"

def test_spaces_at_start_and_end_with_consecutive():
    assert fix_spaces("   Example   1   ") == "-Example-1-"