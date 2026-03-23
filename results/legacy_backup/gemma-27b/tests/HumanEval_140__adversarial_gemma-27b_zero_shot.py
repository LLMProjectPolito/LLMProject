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
        assert fix_spaces("Example   3") == "Example-3"

    def test_trailing_space(self):
        assert fix_spaces("Example 1 ") == "Example_1_"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces(" Example 1 ") == "_Example_1_"

    def test_multiple_spaces_at_beginning(self):
        assert fix_spaces("   Example") == "-Example"

    def test_multiple_spaces_at_end(self):
        assert fix_spaces("Example   ") == "Example-"

    def test_multiple_spaces_in_middle(self):
        assert fix_spaces("Example   Test") == "Example-Test"

    def test_more_than_three_spaces(self):
        assert fix_spaces("Example    Test") == "Example-Test"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_mixed_spaces(self):
        assert fix_spaces("  Example  Test   ") == "_Example-Test-"

    def test_tab_character(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_newline_character(self):
        assert fix_spaces("Example\n1") == "Example_1"

    def test_carriage_return_character(self):
        assert fix_spaces("Example\r1") == "Example_1"