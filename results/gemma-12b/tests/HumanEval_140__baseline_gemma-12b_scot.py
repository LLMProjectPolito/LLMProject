
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
# The function `fix_spaces` aims to modify a given string by replacing spaces with underscores.
# However, it introduces a special rule: if there are more than two consecutive spaces,
# those consecutive spaces should be replaced with a single hyphen.
# The test suite needs to cover various scenarios, including:
# - Empty string
# - String with no spaces
# - String with single spaces
# - String with multiple spaces (less than or equal to 2)
# - String with more than 2 consecutive spaces
# - String with leading/trailing spaces
# - String with a mix of single, double, and multiple spaces.
# - String with special characters.

# STEP 2: PLAN
# Test functions:
# - test_empty_string: Checks the behavior with an empty string.
# - test_no_spaces: Checks the behavior with a string containing no spaces.
# - test_single_space: Checks the behavior with a string containing a single space.
# - test_double_spaces: Checks the behavior with a string containing two spaces.
# - test_triple_spaces: Checks the behavior with a string containing three or more consecutive spaces.
# - test_leading_spaces: Checks the behavior with leading spaces.
# - test_trailing_spaces: Checks the behavior with trailing spaces.
# - test_mixed_spaces: Checks the behavior with a mix of single, double, and multiple spaces.
# - test_special_characters: Checks the behavior with special characters in the string.
# - test_string_with_numbers: Checks the behavior with numbers in the string.

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
    result = ""
    i = 0
    while i < len(text):
        if text[i] == ' ':
            if i + 1 < len(text) and text[i+1] == ' ' and i + 2 < len(text) and text[i+2] == ' ':
                result += "-"
                i += 3
            else:
                result += "_"
                i += 1
        else:
            result += text[i]
            i += 1
    return result

class TestFixSpaces:
    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_double_spaces(self):
        assert fix_spaces("Example  1") == "Example__1"

    def test_triple_spaces(self):
        assert fix_spaces("Example   1") == "Example-1"

    def test_leading_spaces(self):
        assert fix_spaces(" Example") == "_Example"

    def test_trailing_spaces(self):
        assert fix_spaces("Example ") == "Example_"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2") == "Example__1-2"

    def test_special_characters(self):
        assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&*()"

    def test_string_with_numbers(self):
        assert fix_spaces("1 2 3   4") == "1_2_3-4"