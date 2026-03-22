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

    def test_multiple_spaces_only(self):
        assert fix_spaces("   ") == "-"

    def test_mixed_spaces(self):
        assert fix_spaces("  Example   1  ") == "_Example-1_"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_string_with_tabs(self):
        assert fix_spaces("Example\t1") == "Example\t1"

    def test_string_with_newlines(self):
        assert fix_spaces("Example\n1") == "Example\n1"

    def test_long_string_with_multiple_spaces(self):
        long_string = "This is a very long string with   multiple   spaces."
        assert fix_spaces(long_string) == "This_is_a_very_long_string_with-multiple-spaces."

    def test_three_consecutive_spaces(self):
        assert fix_spaces("abc   def") == "abc-def"

    def test_four_consecutive_spaces(self):
        assert fix_spaces("abc    def") == "abc-def"

    def test_more_than_three_consecutive_spaces(self):
        assert fix_spaces("abc     def") == "abc-def"

    def test_leading_and_trailing_spaces_with_multiple_in_between(self):
        assert fix_spaces("  abc   def  ") == "_abc-def_"