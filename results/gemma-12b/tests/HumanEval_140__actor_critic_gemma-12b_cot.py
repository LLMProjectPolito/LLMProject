
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
import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 

    This function only replaces spaces. Tabs and newlines are not modified.

    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = text.replace(" ", "_")
    text = re.sub(r"{2,}", "-", text)
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
        """Tests that consecutive spaces are replaced with a hyphen."""
        assert fix_spaces("Example  1") == "Example-1"
        assert fix_spaces("Example   1") == "Example-1"
        assert fix_spaces("Example    1") == "Example-1"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2") == "Example-1-2"

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_string_with_tabs(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_string_with_newlines(self):
        assert fix_spaces("Example\n1") == "Example_1"

    def test_string_with_special_characters(self):
        assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&*()"

    def test_string_with_numbers(self):
        assert fix_spaces("Example 123 456") == "Example_123_456"

    def test_long_string(self):
        long_string = "This is a very long string with many spaces.   It should be fixed correctly."
        expected_result = "This_is_a_very_long_string_with_many_spaces.-It_should_be_fixed_correctly."
        assert fix_spaces(long_string) == expected_result

    def test_leading_and_trailing_spaces(self):
        """Tests a string with spaces at the beginning and end."""
        assert fix_spaces(" Example ") == "_-Example-_"

    def test_single_space_at_beginning_and_end(self):
        """Tests a string with a single space at the beginning and end."""
        assert fix_spaces(" Example ") == "_-Example-_"