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
    space_count = 0
    for char in text:
        if char.isspace():
            space_count += 1
            if space_count > 2:
                result += '-'
            else:
                result += '_'
        else:
            result += char
            space_count = 0
    return result

class TestFixSpaces:
    def test_no_spaces(self):
        assert fix_spaces("Example") == "Example"

    def test_single_space(self):
        assert fix_spaces("Example 1") == "Example_1"

    def test_leading_space(self):
        assert fix_spaces(" Example 2") == "_Example_2"

    def test_trailing_space(self):
        assert fix_spaces("Example 2 ") == "Example_2_"

    def test_leading_and_trailing_spaces(self):
        assert fix_spaces(" Example 2 ") == "_Example_2_"

    def test_consecutive_spaces_more_than_two(self):
        assert fix_spaces(" Example   3") == "_Example-3"

    def test_consecutive_spaces_at_beginning(self):
        assert fix_spaces("   Example 4") == "-Example_4"

    def test_consecutive_spaces_at_end(self):
        assert fix_spaces("Example 5   ") == "Example_5-"

    def test_mixed_spaces(self):
        assert fix_spaces("Example  1   2  3") == "Example-1-2_3"

    def test_empty_string(self):
        assert fix_spaces("") == ""

    def test_string_with_only_spaces(self):
        assert fix_spaces("   ") == "-"

    def test_exactly_two_consecutive_spaces(self):
        assert fix_spaces("Example  1") == "Example_1"

    def test_consecutive_spaces_at_both_ends(self):
        assert fix_spaces("  Example  ") == "-Example-"

    def test_multiple_consecutive_spaces(self):
        assert fix_spaces(" Example     4") == "_Example----4"

    def test_string_with_tabs(self):
        assert fix_spaces("Example\t1") == "Example_1"

    def test_string_with_mixed_whitespace(self):
        assert fix_spaces("Example \t 1  \n2") == "Example_1-2"

    def test_long_string(self):
        long_string = " " * 100
        assert fix_spaces(long_string) == "-" * 100