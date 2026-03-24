
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
    if "   " in text:
        return text.replace("   ", "-")
    else:
        return text.replace(" ", "_")

class TestFixSpaces:

    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_multiple_spaces(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_trailing_space(self):
        assert fix_spaces("Example 1 ") == "Example_1_"

    def test_multiple_leading_and_trailing_spaces(self):
        assert fix_spaces("  Example  ") == "_Example_"

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_mix_of_single_and_multiple_spaces(self):
        assert fix_spaces("Example  1 2   3") == "Example-1_2-3"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_string_with_tabs(self):
        assert fix_spaces("Example\t1") == "Example\t1"

    def test_string_with_newlines(self):
        assert fix_spaces("Example\n1") == "Example\n1"

    def test_long_string_with_multiple_space_groups(self):
        long_string = "This is a long string with   multiple   space   groups."
        assert fix_spaces(long_string) == "This_is_a_long_string_with-multiple-space-groups."

    def test_three_consecutive_spaces(self):
        assert fix_spaces("abc   def") == "abc-def"

    def test_four_consecutive_spaces(self):
        assert fix_spaces("abc    def") == "abc-def"