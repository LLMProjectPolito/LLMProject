
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
    result = ""
    count = 0
    for char in text:
        if char == ' ':
            count += 1
            if count <= 2:
                result += "_"
        else:
            count = 0
            result += char
    return result

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `fix_spaces` aims to replace spaces in a string with underscores.
# If there are more than two consecutive spaces, it replaces them with a hyphen.
# The function should handle empty strings, strings with no spaces, strings with single spaces,
# strings with multiple spaces, and strings with more than two consecutive spaces.
# Edge cases include empty string, string with only spaces, string with leading/trailing spaces.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_string: Test with an empty string.
# test_no_spaces: Test with a string containing no spaces.
# test_single_space: Test with a string containing a single space.
# test_multiple_spaces: Test with a string containing multiple spaces.
# test_consecutive_spaces: Test with a string containing more than two consecutive spaces.
# test_leading_trailing_spaces: Test with a string containing leading and trailing spaces.
# test_mixed_spaces: Test with a string containing a mix of spaces and other characters.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_string():
    assert fix_spaces("") == ""

def test_no_spaces():
    assert fix_spaces("Example") == "Example"

def test_single_space():
    assert fix_spaces("Example 1") == "Example_1"

def test_multiple_spaces():
    assert fix_spaces(" Example 2") == "_Example_2"

def test_consecutive_spaces():
    assert fix_spaces(" Example   3") == "_Example-3"

def test_leading_trailing_spaces():
    assert fix_spaces("  Hello World  ") == "_Hello_World_"

def test_mixed_spaces():
    assert fix_spaces("This is a test string.  ") == "This_is_a_test_string__"

def test_all_spaces():
    assert fix_spaces("   ") == "--"

def test_long_consecutive_spaces():
    assert fix_spaces("This has many   spaces   in a row.") == "This_has_many---spaces---in_a_row."