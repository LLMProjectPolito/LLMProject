import pytest
import re

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
    text = re.sub(r"{3,}", "-", text)
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

    def test_multiple_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_consecutive_spaces_at_start(self):
        assert fix_spaces("  Example 4") == "-Example_4"

    def test_consecutive_spaces_at_end(self):
        assert fix_spaces("Example 5  ") == "Example_5-"

    def test_consecutive_spaces_in_middle(self):
        assert fix_spaces("Example   6  ") == "Example-6-"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces("Example     7") == "Example--------7"

    def test_mixed_spaces(self):
        assert fix_spaces(" Example  8  Example ") == "_Example-8-_Example_"

    def test_string_with_only_spaces(self):
        assert fix_spaces("   ") == "---"

    def test_string_with_more_than_3_consecutive_spaces(self):
        assert fix_spaces("Example  EEEE  ") == "Example------EEEE-"

    def test_string_with_only_4_consecutive_spaces(self):
        assert fix_spaces("    ") == "----"

    def test_mixed_consecutive_spaces(self):
        assert fix_spaces("  Example   EEEE ") == "-Example-EEEE-"

    def test_mixed_consecutive_spaces_2_3_4(self):
        assert fix_spaces("  Example   EEEE ") == "-Example-EEEE-"

    def test_string_with_tabs(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_string_with_newlines(self):
        assert fix_spaces("Example\n1") == "Example_1"

    def test_string_with_special_characters(self):
        assert fix_spaces("Example!@#$%^&*()") == "Example!@#$%^&_()*"

    def test_unicode_space(self):
        assert fix_spaces("Example\u00A01") == "Example_1"

    def test_mixed_whitespace(self):
        assert fix_spaces("Example\t  1\n2") == "Example_	-1_2"