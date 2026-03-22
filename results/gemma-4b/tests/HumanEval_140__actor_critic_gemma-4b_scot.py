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
    while "  " in text:
        text = text.replace("  ", "-")
    return text.replace(" ", "_")

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `fix_spaces` aims to replace spaces in a string with underscores.
# If there are more than two consecutive spaces, they should be replaced with hyphens.
# The function should handle empty strings and strings with no spaces correctly.
# Edge cases include: empty string, single space, multiple spaces, consecutive spaces, leading/trailing spaces.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_string: Test with an empty string.
# test_no_spaces: Test with a string containing no spaces.
# test_single_space: Test with a string containing a single space.
# test_multiple_spaces: Test with a string containing multiple spaces.
# test_consecutive_spaces: Test with a string containing consecutive spaces.
# test_leading_trailing_spaces: Test with a string containing leading and trailing spaces.
# test_mixed_spaces: Test with a string containing a mix of spaces and other characters.
# test_consecutive_and_mixed: Test with a string containing consecutive spaces and mixed characters.
# test_long_string: Test with a long string to check performance and edge cases.


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
    assert fix_spaces("  Example  ") == "_Example_"

def test_mixed_spaces():
    assert fix_spaces("Hello   World!") == "Hello_World!"

def test_consecutive_and_mixed():
    assert fix_spaces("Hello  World   Test") == "Hello_World-Test"

def test_long_string():
    long_string = "This is a very long string with many spaces and some consecutive spaces."
    expected_result = "This_is_a_very_long_string_with_many_spaces_and_some_consecutive_spaces."
    assert fix_spaces(long_string) == expected_result