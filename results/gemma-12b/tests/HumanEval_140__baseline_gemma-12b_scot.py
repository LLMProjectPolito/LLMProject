
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

# STEP 1: REASONING
# The function `fix_spaces` aims to modify a given string by replacing spaces with underscores and handling consecutive spaces.
# The core logic involves two replacements:
# 1. Single spaces are replaced with underscores.
# 2. More than two consecutive spaces are replaced with hyphens.
# The test suite needs to cover various scenarios, including:
# - Empty string
# - String with no spaces
# - String with single spaces
# - String with leading spaces
# - String with trailing spaces
# - String with multiple consecutive spaces (more than 2)
# - String with a mix of single and consecutive spaces
# - String with only consecutive spaces (more than 2)
# - String with consecutive spaces at the beginning
# - String with consecutive spaces at the end

# STEP 2: PLAN
# Test functions:
# - test_empty_string: Checks the behavior with an empty string.
# - test_no_spaces: Checks the behavior with a string containing no spaces.
# - test_single_space: Checks the behavior with a string containing a single space.
# - test_leading_space: Checks the behavior with a string containing a leading space.
# - test_trailing_space: Checks the behavior with a string containing a trailing space.
# - test_multiple_consecutive_spaces: Checks the behavior with multiple consecutive spaces (more than 2).
# - test_mixed_spaces: Checks the behavior with a mix of single and consecutive spaces.
# - test_only_consecutive_spaces: Checks the behavior with only consecutive spaces (more than 2).
# - test_consecutive_spaces_at_beginning: Checks consecutive spaces at the beginning.
# - test_consecutive_spaces_at_end: Checks consecutive spaces at the end.

# STEP 3: CODE
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
    text = text.replace(" ", "_")
    while "  " in text:
        text = text.replace("  ", "-")
    return text

class TestFixSpaces:
    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_trailing_space(self):
        assert fix_spaces("Example 3 ") == "Example_3_"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1  2") == "Example--1_2"

    def test_only_consecutive_spaces(self):
        assert fix_spaces("  3   4") == "-3-4"

    def test_consecutive_spaces_at_beginning(self):
        assert fix_spaces("   Example") == "-Example"

    def test_consecutive_spaces_at_end(self):
        assert fix_spaces("Example   ") == "Example-"